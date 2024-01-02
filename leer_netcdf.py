#%%
import xarray as xr
# import os
# Ruta al archivo NetCDF
# file_path = "ruta/del/archivo.nc"
file_path = "/media/seba/20EABB19EABAEA64/GIS/vscode/miwrfhydro/FORCING/2023-01-01T03_00_00.000000000.LDASIN_DOMAIN4.nc"
# Leer el archivo NetCDF
data = xr.open_dataset(file_path)
# data = xr.open_dataset(file_path, engine='netcdf4')

# Imprimir información del conjunto de datos
print(data)

# data['U_GRD_L103'].isel(time=500).plot.contourf()

#%%
import cartopy.crs as ccrs 
import cartopy.feature as cf
import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=2, ncols=4, subplot_kw=dict(projection=ccrs.PlateCarree()), facecolor='w', figsize=(20, 4))

# plotea la variable temperatura TMP_L1
contour_temp = ax[0,0].contourf(data['lon'], data['lat'], data['TMP_L1'].isel(time=500))
ax[0,0].coastlines('10m')
ax[0,0].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[0,0].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[0,0].set_title('Temperatura')
fig.colorbar(contour_temp, ax=ax[0,0], orientation='vertical', label='Temperatura (°C)')

# plotea la variable presión atmosférica PRES_L1
contour_pres = ax[0,1].contourf(data['lon'], data['lat'], data['PRES_L1'].isel(time=500))
ax[0,1].coastlines('10m')
ax[0,1].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[0,1].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[0,1].set_title('Presión Atmosférica')
fig.colorbar(contour_pres, ax=ax[0,1], orientation='vertical', label='Presión Atmosférica (Pa)')

# plotea la variable humedad específica SPF_H_L103 
contour_humidity = ax[0,2].contourf(data['lon'], data['lat'], data['SPF_H_L103'].isel(time=500))
ax[0,2].coastlines('10m')
ax[0,2].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[0,2].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[0,2].set_title('Humedad Específica')
fig.colorbar(contour_humidity, ax=ax[0,2], orientation='vertical', label='Humedad Específica')

# plotea la variable componente U del viento U_GRD_L103
contour_u_wind = ax[0,3].contourf(data['lon'], data['lat'], data['U_GRD_L103'].isel(time=500))
ax[0,3].coastlines('10m')
ax[0,3].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[0,3].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[0,3].set_title('Componente U del Viento')
fig.colorbar(contour_u_wind, ax=ax[0,3], orientation='vertical', label='Velocidad (m/s)')

# plotea la variable componente V del viento V_GRD_L103
contour_v_wind = ax[1,0].contourf(data['lon'], data['lat'], data['V_GRD_L103'].isel(time=500))
ax[1,0].coastlines('10m')
ax[1,0].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[1,0].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[1,0].set_title('Componente V del Viento')
fig.colorbar(contour_v_wind, ax=ax[1,0], orientation='vertical', label='Velocidad (m/s)')

# plotea la variable ratio de precipitación PRATE_L1_Avg_1  
contour_precipitation = ax[1,1].contourf(data['lon'], data['lat'], data['PRATE_L1_Avg_1'].isel(time=500))
ax[1,1].coastlines('10m')
ax[1,1].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[1,1].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[1,1].set_title('Ratio de Precipitación')
fig.colorbar(contour_precipitation, ax=ax[1,1], orientation='vertical', label='Ratio de Precipitación')

# plotea la variable radiación de onda corta insidente DSWRF_L1_Avg_1 
contour_shortwave = ax[1,2].contourf(data['lon'], data['lat'], data['DSWRF_L1_Avg_1'].isel(time=500))
ax[1,2].coastlines('10m')
ax[1,2].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[1,2].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[1,2].set_title('Radiación de Onda Corta Incidente')
fig.colorbar(contour_shortwave, ax=ax[1,2], orientation='vertical', label='Radiación (W/m^2)')

# plotea la variable radiación de onda larga insidente DLWRF_L1_Avg_1  
contour_longwave = ax[1,3].contourf(data['lon'], data['lat'], data['DLWRF_L1_Avg_1'].isel(time=500))
ax[1,3].coastlines('10m')
ax[1,3].add_feature(cf.BORDERS.with_scale('10m'))
gl = ax[1,3].gridlines(draw_labels=True, color='gray', alpha=0.2, linestyle='--')
gl.ylabels_right = False
gl.xlabels_top = False
ax[1,3].set_title('Radiación de Onda Larga Incidente')
fig.colorbar(contour_longwave, ax=ax[1,3], orientation='vertical', label='Radiación (W/m^2)')

# Ajusta el diseño para evitar superposiciones
fig.tight_layout()

# Muestra el gráfico
plt.show()
#%%