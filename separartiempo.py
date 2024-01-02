#%%
import xarray as xr
import pandas as pd
import os
from datetime import datetime

def split_files(input_file):
    # Abre el archivo netCDF usando xarray
    ds = xr.open_dataset(input_file)

    # Obtén las fechas únicas presentes en el archivo
    unique_dates = pd.to_datetime(ds.time.values)

    # Crea la carpeta FORCING si no existe
    output_folder = "FORCING"
    os.makedirs(output_folder, exist_ok=True)

    # Itera sobre las fechas únicas y guarda archivos individuales
    for date in unique_dates:
        # Formatea la fecha según tu nomenclatura
        formatted_date = date.strftime("%Y%m%d%H")

        # Genera el nombre del nuevo archivo en la carpeta FORCING
        output_file = os.path.join(output_folder, f"{formatted_date}.LDASIN_DOMAIN4.nc")

        # Filtra los datos para la fecha actual y guarda el nuevo archivo
        ds.sel(time=date).to_netcdf(output_file)

    print("Archivos separados exitosamente.")

# Uso del script
input_file = "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/combined_output/final_combined_data.nc"
split_files(input_file)
#%%