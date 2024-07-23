import xarray as xr
import os
import gc
import tqdm  # Progress tracker

# Directory to save processed results
output_dir = "/mnt/drive2/processed_results/"
os.makedirs(output_dir, exist_ok=True)

def load_wrfwof(init: str, var: str) -> xr.Dataset:
    start_date = "2021-09-02" if init in ["00Z", "01Z"] else "2021-09-01"
    new_dates = xr.cftime_range(
        start=start_date + " " + init[:-1] + ":00:00",
        end="2021-09-02 " + str((int(init[:-1]) + 6) % 24).zfill(2) + ":00:00",
        freq="5min"
    )

    def load_single_file(n):
        ds_in = xr.open_mfdataset(
            f"/mnt/drive2/wof-runs/{init}/{var}/wrfwof*{str(n).zfill(2)}",
            decode_times=False,
            combine="nested",
            concat_dim="Time"
        )
        ds_in = ds_in.rename({"Time": "time", "south_north": "lat", "west_east": "lon"})
        ds_in["time"] = new_dates
        return ds_in.drop_vars("XTIME")

    ds_list = [load_single_file(n) for n in range(1, 19)]
    ds_concat = xr.concat(ds_list, dim='ne')

    # Rechunk after concatenation
    ds_concat = ds_concat.chunk({"time": 100, "lat": 50, "lon": 50})

    # Decode times after rechunking
    ds_concat = xr.decode_cf(ds_concat)

    # Explicitly trigger garbage collection
    gc.collect()

    return ds_concat

def preprocess_data(output_dir, var):
    all_data = []
    for init in tqdm.tqdm(["20Z", "21Z", "22Z", "23Z"], desc=f"Processing {var}"):
        data = load_wrfwof(init, var)
        all_data.append(data)
    
    # Concatenate along initialization time
    concatenated_data = xr.concat(all_data, dim="init_time")

    # Save to netCDF
    output_file = os.path.join(output_dir, f"concatenated_data_{var}.nc")
    concatenated_data.to_netcdf(output_file)

if __name__ == "__main__":
    variables = ["U_zlev", "V_zlev"]
    for var in variables:
        preprocess_data(output_dir, var)
