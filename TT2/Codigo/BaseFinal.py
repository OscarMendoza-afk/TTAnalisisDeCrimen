import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


dfU = pd.read_csv(r"D:\TT2\Data\BaseUnida.csv" )   #Se carga el archivo CSV como un dataframe

print(dfU.columns)