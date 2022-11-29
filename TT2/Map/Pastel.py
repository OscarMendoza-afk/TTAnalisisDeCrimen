import plotly.express as px
import pandas as pd

# This dataframe has 244 lines, but 4 distinct values for `day`
df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv")
fig = px.pie(df, values='Delito', names='Alcalia')
fig.show()