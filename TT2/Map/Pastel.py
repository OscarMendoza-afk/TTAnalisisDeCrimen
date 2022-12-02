import plotly.express as px
import pandas as pd

crimen="FRAUDE"

# This dataframe has 244 lines, but 4 distinct values for `day`
df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv")

df.drop(df[df['Delito'] != crimen ].index, inplace = True)

fig = px.pie(df, values='Delito', names='Alcalia')
fig.show()