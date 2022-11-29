import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import json
import requests
import pandas as pd
import numpy as np

from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

df['Info'] = '<br>Delito:' + df['Delito'].astype(str) + '<br> Año:' + df['Año'].astype(str)


app.layout = html.Div([
    dcc.Graph(
        id='example-map',
    ),
    dcc.Slider(
        df['Año'].min(),
        df['Año'].max(),
        step=None,
        value=df['Año'].min(),
        marks={str(Año): str(Año) for Año in df['Año'].unique()},
        id='Año-slider'
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('Año-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.Año == selected_year]

    fig = px.density_mapbox(df, lon='longitud', lat='latitud',  radius=10,
                        title="Mapa de calor de " ,
                        color_continuous_scale="inferno",
                        center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,                        
                        hover_name="Alcalia",
                        hover_data=["Info"],
                        mapbox_style="carto-positron")

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)