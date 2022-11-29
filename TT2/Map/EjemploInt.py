from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv")


app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
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
def update_figure(selected_Año):
    filtered_df = df[df.Año == selected_Año]

    fig = px.scatter(filtered_df, x="Delito", y="Hora",
                     color="Sexo", hover_name="Delito",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
