import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np

import dash             #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly          #(version 4.4.1)




#fecha1=int(input('Introduce el primer año>> '))
#fecha2=int(input('Introduce el segundo año>> '))

fecha1=2019
fecha2=2020

crimen="FRAUDE"

alcaldia="COYOACAN"


df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

#print(df.columns)

df['Info'] = '<br>Delito:' + df['Delito'].astype(str) + '<br> Año:' + df['Año'].astype(str)

app = dash.Dash(__name__)

app.layout = html.Div([
        html.Div([
            html.Pre(children= "Delitos en la CDMX de 2018-2021",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ])
])



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

if __name__ == '__main__':
    app.run_server(debug=True)