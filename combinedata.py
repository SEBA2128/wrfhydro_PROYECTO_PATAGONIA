

import os
import xarray as xr
import subprocess  # Importar el módulo subprocess para ejecutar comandos en el sistema

# Directorios de entrada y salida
input_dirs = [
    "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_press_temp",
    "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_specific_humidity",
    "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_u_v_component_wind",
    "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3-hour_Average_lwd_swd_preci"
]

output_dir = "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/combined_output"

# Crear el directorio de salida si no existe
subprocess.run(["mkdir", "-p", output_dir])
# subprocess.run(["sudo", "mkdir", "-p", output_dir])

# Cambiar los permisos del directorio de salida si es necesario
# subprocess.run(["sudo", "chmod", "u+w", output_dir])
subprocess.run(["chmod", "u+w", output_dir])

# Combinar archivos en cada directorio
for input_dir in input_dirs:
    # Obtener la lista de archivos en el directorio
    files = os.listdir(input_dir)
    files = [os.path.join(input_dir, file) for file in files]
    
    # Combinar archivos en un solo archivo NetCDF
    combined_data = xr.open_mfdataset(files, combine="nested", concat_dim="time")
    
    # Guardar el archivo combinado en el directorio de salida
    output_file = os.path.join(output_dir, f"{os.path.basename(input_dir)}_combined.nc")
    combined_data.to_netcdf(output_file)
    
    # Cerrar el conjunto de datos combinado
    combined_data.close()

# Combinar archivos NetCDF en un solo archivo
output_files = [os.path.join(output_dir, f"{os.path.basename(dir)}_combined.nc") for dir in input_dirs]
datasets = [xr.open_dataset(file) for file in output_files]
combined_data = xr.merge(datasets)
combined_data.to_netcdf(os.path.join(output_dir, "final_combined_data.nc"))

# Cerrar los conjuntos de datos originales
for ds in datasets:
    ds.close()

print("Datos combinados exitosamente")
