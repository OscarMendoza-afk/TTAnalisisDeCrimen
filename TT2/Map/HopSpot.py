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

#print(df.columns)

df['Info'] = '<br>Delito:' + df['Delito'].astype(str) + '<br> Año:' + df['Año'].astype(str)


df.drop(df[df['Año'] < fecha1 ].index, inplace = True)  
df.drop(df[df['Año'] > fecha2 ].index, inplace = True)  

df.drop(df[df['Delito'] != crimen ].index, inplace = True)

df.drop(df[df['Alcalia'] != alcaldia ].index, inplace = True)

año1=str(fecha1)
año2=str(fecha2)
de=str(crimen)

fig = px.density_mapbox(df, lon='longitud', lat='latitud',  radius=10,
                        title="Mapa de calor de " + de + " en los años " +  año1 + " - " + año2 ,
                        color_continuous_scale="inferno",
                        center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,                        
                        hover_name="Alcalia",
                        hover_data=["Info"],
                        mapbox_style="carto-positron")
                        
fig.show()