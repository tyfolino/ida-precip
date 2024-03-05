# Import statements
import xarray as xr
import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(
    description="Calculates the height on the native vertical grid."
)

# Add arguments
parser.add_argument("filename", help="The name of the file")
parser.add_argument("path", help="The path of the desired WoFS initialization.")

# Parse arguments
args = parser.parse_args()

# Access arguments
filename = args.filename
path = args.path

# Read in necessary variables
PH = xr.open_dataarray(path+"/PH/"+filename,decode_times=False)
PHB = xr.open_dataarray(path+"/PHB/"+filename,decode_times=False)
P = xr.open_dataarray(path+"/P/"+filename,decode_times=False)

# Calculate height on the staggered grid, then move to centered point
z_stag = (PH + PHB)/9.81
z = 0.5 * (
    z_stag.isel(bottom_top_stag=slice(None,-1)) + 
    z_stag.isel(bottom_top_stag=slice(1,None))
)

# Fix dims & coordinates
z = z.assign_coords(coords=P.coords).reindex_like(P).rename("z")
z = z.rename({"bottom_top_stag":"bottom_top"})

z = z.assign_attrs(
    {
        "units":"m",
        "description":"heights on native vertical grid"
    }
)

# Save out MSLP as netCDF
z.to_netcdf(path+"/z/"+filename)