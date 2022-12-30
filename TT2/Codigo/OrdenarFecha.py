import pandas as pd
import numpy as np


df = pd.read_csv(r"/run/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv" )

print(df.columns)

print(df.Mes)


df['Fecha'] = pd.to_datetime(df.Fecha)

df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')

print(df.Fecha)

df.to_csv("/home/ozkr/Documentos/BaseCrimenes.csv", index=False)