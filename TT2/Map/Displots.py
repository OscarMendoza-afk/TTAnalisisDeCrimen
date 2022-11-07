import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np


#fecha=int(input('Introduce el año>> '))


df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

fig = px.histogram(df, 
                    x="Mes", 
                    y="Delito", 
                    #color="Sexo", 
                    #marginal="rug",
                   hover_data=df.columns)
fig.show()