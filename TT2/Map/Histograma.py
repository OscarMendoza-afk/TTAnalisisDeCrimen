import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import json
import requests
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )





app.layout = html.Div(children=[
    html.H1(children='Delitos por Sexo'),

    html.Div(children='''
        Conteo de delitos y comparación por sexo
    '''),

    dcc.Dropdown(
                df['Delito'].unique(),
                'Delito',
                id='xaxis-column'
            ), 

    dcc.Graph(
        id='indicator-graphic'
    )
])





@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    )
def update_graph(xaxis_column_name):

    fig = px.histogram(df[df['Delito'] == xaxis_column_name]['Value'], x="Delito", color="Sexo", barmode="group")

    fig.update_xaxes(title=xaxis_column_name)

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
