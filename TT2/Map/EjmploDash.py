from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

fecha1=2019
fecha2=2020


df.drop(df[df['Año'] < fecha1 ].index, inplace = True)  
df.drop(df[df['Año'] > fecha2 ].index, inplace = True)  



fig = px.bar(df, x="Delito", y="Mes", color="Sexo", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Delitos Por Mes y Sexo'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

