import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


#Se carga el archivo CSV como un dataframe

df = pd.read_csv(r"D:\TT2\Data\BaseLimpiaUpdate.csv")


df.drop(df[df['Alcalia'] != 'XOCHIMILCO' ].index, inplace = True) 


df.to_csv("XOCHIMILCO.csv", index=False)
