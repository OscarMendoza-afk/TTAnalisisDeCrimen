#Importar librer√≠as
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import requests
import json

shapefile = '/home/ozkr/Documentos/alcaldías_cdmx/alcaldias_cdmx.shp'

gg = gpd.read_file(shapefile, encoding='utf-8')

poligonos=pd.read_csv(r"/home/ozkr/Documentos/PoligonosCDMX.csv")

gdf = gpd.read_file(shapefile, encoding='utf-8')

df = pd.read_csv(r"/home/ozkr/Documentos/NumDelitosalcladia.csv")

with open('/home/ozkr/Documentos/AlcaldiasshapeCDMX.json') as data_file:    
    d= json.load(data_file)  

#datos = pd.read_json(r'/home/ozkr/Documentos/AlcaldiasshapeCDMX.json')

#alcaldias_geo=requests.get(jsonfile).json()

#print(gdf.columns)

#print(gdf['geometry'])

'''
dfA=df["Alcaldia"].value_counts()
print(dfA)

dfA=dfA.to_frame()

dfA['index'] = dfA.index
dfA=dfA.reset_index()
dfA=dfA[['index','Alcaldia']]

dfA=dfA.rename(columns={'index' :'Alcaldia', 'Alcaldia' :'NumDelitos'})

print(dfA)

dfA.to_csv("/home/ozkr/Documentos/NumDelitosalcladia.csv", index=False)
'''


gdf=gdf[['cve_mun','geo_shp']]


gdf=gdf.replace({9:'MILPA ALTA', 14:'BENITO JUAREZ', 5:'GUSTAVO A MADERO', 3:'COYOACAN', 16:'MIGUEL HIDALGO', 8:'LA MAGDALENA CONTRERAS', 11:'TLAHUAC', 2:'AZCAPOTZALCO', 6:'IZTACALCO', 10:'ALVARO OBREGON', 13:'XOCHIMILCO', 17:'VENUSTIANO CARRANZA', 12:'TLALPAN', 4:'CUAJIMALPA DE MORELOS', 15:'CUAUHTEMOC', 7:'IZTAPALAPA' })

gdf=gdf.rename(columns={'cve_mun':'Alcaldia'})

#gdf.to_csv("/home/ozkr/Documentos/PoligonosCDMX.csv", index=False)

dfF=pd.merge(df, gdf, on='Alcaldia')

#dfF.to_csv("/home/ozkr/Documentos/ShapeAlcaldias.csv", index=False)

#print(gdf.columns)

#print(gdf.head)

#dfF.plot()



#merged_json = json.loads(d.to_json())

#Convertir objeto a string
#json_data = json.dumps(merged_json)

'''
#Max Color
max_color = datos['NumDelitos'].max()

#Cargar la data json_data
gsource = GeoJSONDataSource(geojson = json_data)

#Definir una paleta de colores
colores = brewer['YlGnBu'][9]

#Revertir la paleta para que a mayor número, mas oscuro
colores = colores[::-1]

#Inicializar LinearColorMapper. Para que asocie un número a los colores.
color_mapper = LinearColorMapper(palette = colores, low = 0, high = max_color)

#Agregar hovers
hover = HoverTool(tooltips = [('Alcaldia','@Alcaldia'), ('NumDelitos', '@NumDelitos')])

#Crear el objeto figura
fig = figure(title = 'Delitos por Alcaldia',
          #plot_height = 600,
          #plot_width = 950,
          toolbar_location = None,
          tools = [hover])

fig.xgrid.grid_line_color = None
fig.ygrid.grid_line_color = None
fig.title.text_font_size = '20pt'

#Ocultamos los ejes
fig.axis.visible = False

#Agregar comunas
fig.patches('xs', 'ys', 
          source = gsource,
          fill_color = {'field': 'NumDelitos', 'transform': color_mapper},
          line_color = 'black',
          line_width = 0.25,
          fill_alpha = 1,
          name = 'Alcaldias')

#Display
output_notebook()
show(fig)
#Guardar HTML
output_file('Mapa_RM.html')
save(fig)
'''

fig = px.choropleth(data_frame=dfF, 
                    geojson=d, 
                    locations='Alcaldia', # nombre de la columna del Dataframe
                    featureidkey='properties.nomgeo',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='NumDelitos', #El color depende de las cantidades
                    color_continuous_scale="burg", #greens
                    #scope="north america"
                   )
fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

fig.update_layout(
    title_text = 'Mapa de Coropletas de Alcaldias más Delictivas',
    font=dict(
        #family="Courier New, monospace",
        family="Ubuntu",
        size=18,
        color="#7f7f7f"
    ),
    annotations = [dict(
        x=0.55,
        y=-0.1,
        xref='paper',
        yref='paper',
        text='Fuente: Portal de Datos Abiertos México',
        showarrow = False
    )]
)

fig.show()

fig.write_html("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/Map/MapasHTML/Coropletas.html")






