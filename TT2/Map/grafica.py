from django.urls import reverse_lazy
import plotly.express as px
import pandas as pd

dfU = pd.read_csv(r"/home/ozkr/Documentos/UpdateCrimenesCleanV.csv")
print(dfU.columns)

dfU.drop(dfU[dfU['Año'] <= 2017 ].index, inplace = True)  

#dfS = dfS[dfS['Año_hecho'].notna()] #se eliminan las filas con el espacio en blnaco

dfU.drop(dfU[dfU['Año'] >= 2019 ].index, inplace = True)  

dfFreq = dfU.groupby(['Fecha']).size().to_frame().reset_index()
dfFreq.columns = ['fecha', 'ocurrencia']

fig = px.line(dfFreq, x='fecha', y='ocurrencia', markers=True)

fig.write_html("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/Map/MapasHTML/Grafica.html")



