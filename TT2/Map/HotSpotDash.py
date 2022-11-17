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

app.layout = html.Div([
    dcc.Slider(0, 20, 5,
               value=10,
               verticalHeight=200 ,
               id='my-slider'
    ),
    html.Div(id='slider-output-container')
])

@app.callback(
    Output('slider-output-container', 'children'),
    Input('my-slider', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)



if __name__ == '__main__':
    app.run_server(debug=True)
