import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


#Se carga el archivo CSV como un dataframe

df = pd.read_csv(r"C:\Users\ozkr_\Downloads\BaseLimpiaUpdate.csv")


df.drop(df[df['Alcalia'] != 'AZCAPOTZALCO' ].index, inplace = True) 


df.to_csv("AZCAPOTZALCO.csv", index=False)
