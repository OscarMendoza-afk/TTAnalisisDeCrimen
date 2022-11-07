import plotly.graph_objects as go
import plotly.express as px
import json
import requests
import pandas as pd
import numpy as np



df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )


# Here we use a column with categorical data
fig = px.histogram(df, x="Mes")
fig.show()