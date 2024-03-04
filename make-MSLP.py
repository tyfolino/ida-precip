# Import statements
import xarray as xr
from wofs.post.wofs_cbook import calc_mslp
import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(
    description="Calculates the mean sea level pressure."
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
T2 = xr.open_dataarray(path+"/T2/"+filename)
HGT = xr.open_dataarray(path+"/HGT/"+filename)
PSFC = xr.open_dataarray(path+"/PSFC/"+filename)

# Calculate MSLP
MSLP = calc_mslp(T2,HGT,PSFC)
MSLP = MSLP.rename("MSLP") * 100
MSLP.attrs["units"] = 'Pa'

# Save out MSLP as netCDF
MSLP.to_netcdf(path+"/MSLP/"+filename)
