import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


#Se carga el archivo CSV como un dataframe

df = pd.read_csv(r"/media/ozkr/Datos/TT2/Data/BaseLimpiaUpdate.csv")

print(df.columns)
print(df.head)

print(df['Delito'])

df.drop(df[df['Alcalia'] != 'AZCAPOTZALCO' ].index, inplace = True) 

df.drop(df[df['Delito'] != 'FRAUDE' ].index, inplace = True) 

print(df.head)

df.to_csv("/home/ozkr/Documentos/alcaldias/AZCAPOTZALCOfraude.csv", index=False)
