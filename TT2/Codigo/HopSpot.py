import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np


fecha=int(input('Introduce el año>> '))

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

#print(df.columns)

df['etiqueta'] = df['Alcalia'].astype(str) + '<br>' + df['Delito'].astype(str)


df.drop(df[df['Año'] <= fecha ].index, inplace = True)  
df.drop(df[df['Año'] >= fecha ].index, inplace = True)  

año=str(fecha)

fig = px.density_mapbox(df, lon='longitud', lat='latitud',  radius=10,
                        title="Mapa de calor por año (" +  año + ")" ,
                        color_continuous_scale="inferno",
                        center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,                        
                        hover_name="Alcalia",
                        hover_data=["Delito"],
                        mapbox_style="carto-positron")


                        
fig.show()