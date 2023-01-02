import pandas as pd
import numpy as np


df = pd.read_csv(r"/home/ozkr/Documentos/UpdateCrimenesENE.csv" )

print(df.columns)

print(df.Mes)


df['Fecha'] = pd.to_datetime(df.Fecha)

df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')

print(df.Fecha)

df.to_csv("/home/ozkr/Documentos/UpdateCrimenesENE.csv", index=False)