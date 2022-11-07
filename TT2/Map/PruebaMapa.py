import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np


df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

print(df.columns)

df['etiqueta'] = df['Alcalia'].astype(str) + '<br>' + df['Delito'].astype(str)

geoJSONFile = 'Centrar.json'
with open(geoJSONFile) as response:
    centrar = json.load(response)

#Filtrar años de estudio

df.drop(df[df['Año'] <= 2015 ].index, inplace = True)  
df.drop(df[df['Año'] >= 2015 ].index, inplace = True)  


fig = go.Figure(data=go.Scattergeo(
        lon = df['longitud'],
        lat = df['latitud'],
        text = df['etiqueta'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
           # color = df['cnt'],
            cmax = 10000,
            colorbar_title="Incoming flights<br>February 2011"
        )))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo = dict(
            geojson=response,
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
fig.show()


