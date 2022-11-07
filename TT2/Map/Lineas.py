import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np


#fecha=int(input('Introduce el año>> '))

Alcaldia="COYOACAN"

Delito='FRAUDE'

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

print(df.columns)

df.drop(df[df['Alcalia'] != Alcaldia ].index, inplace = True)
df.drop(df[df['Delito'] != Delito ].index, inplace = True)

#df = df.astype({'Año': 'int32'})

print(df.dtypes)

fig = px.line(df, 
        x="Año", 
        y="Mes", 
        color='Delito'
        )
fig.show()