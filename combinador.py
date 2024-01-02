
#%%
import os
import xarray as xr
import subprocess  # Importar el módulo subprocess para ejecutar comandos en el sistema

from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Ruta de las carpetas de entrada
carpetas_entrada = ["/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3-hour_Average_lwd_swd_preci", "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_press_temp", "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_specific_humidity", "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/3h_forecast_u_v_component_wind"]


# Carpeta de salida
carpeta_salida = "/home/seba/TESIS/FORCING"

# Crear la carpeta de salida si no existe
#Path(carpeta_salida).mkdir(parents=True, exist_ok=True)

# Crear el directorio de salida si no existe
subprocess.run(["mkdir", "-p", carpeta_salida])
# subprocess.run(["sudo", "mkdir", "-p", output_dir])

# Cambiar los permisos del directorio de salida si es necesario
#subprocess.run(["sudo", "chmod", "u+w", output_dir])
subprocess.run(["chmod", "u+w", carpeta_salida])


# Crear un diccionario para almacenar datos por fecha
datos_por_fecha = defaultdict(list)

# Leer archivos de cada carpeta
for carpeta in carpetas_entrada:
    archivos = os.listdir(carpeta)
    
    for archivo in archivos:
        # Combinar ruta de la carpeta con el nombre del archivo
        ruta_archivo = os.path.join(carpeta, archivo)
        
        # Leer el conjunto de datos usando xarray
        ds = xr.open_dataset(ruta_archivo)
        
        # Verificar si 'time_bnds' está presente
        if 'time_bnds' not in ds.variables:
            print(f"Advertencia: 'time_bnds' no está presente en {ruta_archivo}")
            continue

        # Extraer la fecha del archivo (ajusta esto según la estructura de tus archivos)
        fecha = ds["time"].values[0]
        fecha_str = str(fecha)  # Convertir a cadena
        
        # Agregar el conjunto de datos al diccionario
        datos_por_fecha[fecha_str].append(ds)

# Guardar los conjuntos de datos combinados en la carpeta de salida
for fecha, conjuntos_datos in datos_por_fecha.items():
    # Concatenar conjuntos de datos
    ds_combinado = xr.concat(conjuntos_datos, dim="variable")
    
    # Crear nombre de archivo de salida
    nombre_archivo = f"{fecha}.LDASIN_DOMAIN4.nc"
    
    # Ruta de salida
    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
    
    # Guardar el conjunto de datos combinado
    ds_combinado.to_netcdf(ruta_salida)

print("Proceso completado.")

# %%
