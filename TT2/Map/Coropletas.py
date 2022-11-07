import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np

fecha1=int(input('Introduce el primer año>> '))
fecha2=int(input('Introduce el segundo año>> '))

crimen="FRAUDE"

alcaldia="COYOACAN"


df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

fig = px.choropleth_mapbox(df, lon='longitud', lat='latitud',
                           geojson='/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/Map/coloniascdmx.geojson',
                           color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,
                           opacity=0.5,
                           labels={'Alcalia':'Delito'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()