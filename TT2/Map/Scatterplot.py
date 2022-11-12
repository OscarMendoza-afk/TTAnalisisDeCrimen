import pandas as pd     #(version 0.24.2)

import dash             #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly          #(version 4.4.1)
import plotly.express as px

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

mark_values = {2018:'2018',2019:'2019',2020:'2020',2021:'2021'}

app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
        html.Div([
            html.Pre(children= "Delitos en la CDMX de 2018-2021",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ]),

        html.Div([
            dcc.RangeSlider(id='the_year',
                min=2018,
                max=2021,
                value=[2018,2021],
                marks=mark_values,
                step=None)
        ],style={"width": "70%", "position":"absolute",
                 "left":"5%"})

])
#---------------------------------------------------------------
@app.callback(
    Output('the_graph','figure'),
    [Input('the_year','value')]
)

def update_graph(years_chosen):
    print(years_chosen)

    dff=df[(df['Año']>=years_chosen[0])&(df['Año']<=years_chosen[1])]
    # filter df rows where column year values are >=1985 AND <=1988
    dff=dff.groupby(["Delito"], as_index=False)["Alcalia",
                    "Delito"].mean()
    #print (dff[:3])

    fig = px.density_mapbox(df, lon='longitud', lat='latitud',  radius=10,
                        #title="Mapa de calor de " + de + " en los años " +  año1 + " - " + año2 ,
                        color_continuous_scale="inferno",
                        center=dict(lon=-99.1374477062327, lat=19.402765630374645), zoom=9,                        
                        hover_name="Alcalia",
                        hover_data=["Info"],
                        mapbox_style="carto-positron")

    fig.update_traces()

    return (fig)

if __name__ == '__main__':
    app.run_server(debug=True)