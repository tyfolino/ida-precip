# import statements
import wrf.destag
import xarray as xr
import numpy as np
import argparse
from xgcm import Grid
from pathlib import Path
import wrf

def make_z(filename: str, path: str) -> None:
    # If z directory doesn't already exist, make one
    Path(path+"/z").mkdir(parents=True,exist_ok=True)
    # Read in necessary variables
    ph = xr.open_dataarray(path+"/PH/"+filename,decode_times=False)
    phb = xr.open_dataarray(path+"/PHB/"+filename,decode_times=False)
    p = xr.open_dataarray(path+"/P/"+filename,decode_times=False)

    # Calculate height on the staggered grid, then move to centered point
    z_stag = (ph + phb)/9.81
    z = 0.5 * (
        z_stag.isel(bottom_top_stag=slice(None,-1)) + 
        z_stag.isel(bottom_top_stag=slice(1,None))
    )

    # Fix dims & coordinates
    z = z.assign_coords(coords=p.coords).reindex_like(p).rename("z")
    z = z.rename({"bottom_top_stag":"bottom_top"})

    z = z.assign_attrs(
        {
            "units":"m",
            "description":"heights on native vertical grid"
        }
    )

    # Save out height as netCDF
    z.to_netcdf(path+"/z/"+filename)

def make_mslp(filename: str, path: str) -> None:
    # If mslp directory doesn't exist, we need to make it
    Path(path+"/mslp").mkdir(parents=True,exist_ok=True)
    # Read in necessary variables
    t2 = xr.open_dataarray(path+"/T2/"+filename,decode_times=False)
    hgt = xr.open_dataarray(path+"/HGT/"+filename,decode_times=False)
    psfc = xr.open_dataarray(path+"/PSFC/"+filename,decode_times=False)

    # Convert the height to kilometers
    hgt_km = hgt/1000
    
    # Assume global average tropospheric lapse rate
    stemps = t2+(6.5*hgt_km)

    # Calculate mean sea level pressure
    mslp = psfc*np.exp(9.81/(287*stemps)*hgt)*0.01 + (6.7*hgt_km)
    mslp = mslp.rename("mslp") * 100
    mslp.attrs["units"] = 'Pa'

    # Save out MSLP as netCDF
    mslp.to_netcdf(path+"/mslp/"+filename)

def put_var_on_plevs(filename: str, path: str, varname: str) -> None:
    # If varname directory doesn't exist, make it
    Path(path+"/"+varname+"_plev").mkdir(parents=True,exist_ok=True)
    # Read in variables
    p = xr.open_dataarray(path+"/P/"+filename,decode_times=False)
    pb = xr.open_dataarray(path+"/PB/"+filename,decode_times=False)
    var = xr.open_dataarray(path+"/"+varname+"/"+filename,decode_times=False)

    # Create pressure field
    pres = (p + pb).rename('pres')
    ds_pres = xr.merge([pres,var])

    # Create grid and pressure levels
    grid = Grid(ds_pres, coords={"Z":{"center":"bottom_top"}}, periodic=False)
    levels = np.array([92500, 85000, 70000, 50000, 30000, 20000])

    # Regrid
    var_pres = grid.transform(ds_pres[varname],"Z",levels,target_data=ds_pres.pres,
                              method="log")
    var_pres = var_pres.rename(varname)
    
    # Save out variable
    var_pres.to_netcdf(path+"/"+varname+"_plev/"+filename)

def put_var_on_zlevs(filename: str, path: str, varname: str) -> None:
    # If varname directory doesn't exist, make it
    Path(path+"/"+varname+"_zlev").mkdir(parents=True,exist_ok=True)
    # Read in variables
    z = xr.open_dataarray(path+"/z/"+filename,decode_times=False)
    var = xr.open_dataarray(path+"/"+varname+"/"+filename,decode_times=False)

    # We sometimes have to destagger the grid
    if("west_east_stag" in var.dims):
        var = wrf.destagger(var,stagger_dim=-1,meta=True)
        var = var.rename(varname)
    elif("south_north_stag" in var.dims):
        var = wrf.destagger(var,stagger_dim=-2,meta=True)
        var = var.rename(varname)
    else:
        pass

    merged = xr.merge([z,var])

    # Create grid and z levels
    grid = Grid(merged,coords={"Z":{"center":"bottom_top"}},periodic=False)
    levels = np.array([500,1000,2000,3000,4000,5000,6000])

    # Regrid
    var_z = grid.transform(merged[varname],"Z",levels,target_data=merged.z,method="log")
    var_z = var_z.rename(varname)

    # Save out variable
    var_z.to_netcdf(path+"/"+varname+"_zlev/"+filename)

def main():
    parser = argparse.ArgumentParser(description='Calculate variables from WoFS.')
    parser.add_argument('function', type=str, help='Name of the function to call')
    parser.add_argument("filename", help="The name of the file")
    parser.add_argument("path", help="The path of the desired WoFS initialization.")
    parser.add_argument(
        "--varname",nargs="?",const="z",help="The name of the variable to put on\
            different vertical levels.")
    args = parser.parse_args()

    if args.function == 'make_z':
        make_z(args.filename, args.path)
    elif args.function == "make_mslp":
        make_mslp(args.filename, args.path)
    elif args.function == "put_var_on_plevs":
        put_var_on_plevs(args.filename,args.path,args.varname)
    elif args.function == "put_var_on_zlevs":
        put_var_on_zlevs(args.filename,args.path,args.varname)
    # Add more conditions for other functions as needed

if __name__ == "__main__":
    main()