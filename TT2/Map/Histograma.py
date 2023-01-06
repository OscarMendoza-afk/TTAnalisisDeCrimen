import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import json
import requests
import pandas as pd
import numpy as np


df = pd.read_csv(r"/home/ozkr/Documentos/UpdateCrimenesCleanV.csv" )

# Here we use a column with categorical data
fig = px.histogram(df, x="Mes")
fig.show()
fig.write_html("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/Map/MapasHTML/Histograma.html")
