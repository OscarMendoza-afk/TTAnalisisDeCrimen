import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc
import json
import requests
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )


# Here we use a column with categorical data
fig = px.histogram(df, x="Delito", color="Sexo", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Delitos por Sexo'),

    html.Div(children='''
        Conteo de delitos y comparación por sexo
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
