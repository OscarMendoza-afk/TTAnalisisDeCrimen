import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


df = pd.read_csv("D:\TT2\Data\BaseCompletaUTF.csv" )   #Se carga el archivo CSV como un dataframe

print(df.columns)


df = df.drop([
            'tempo', 
            'ao_inicio', 
            'mes_inicio', 
            'fecha_inicio', 
            'agencia', 
            'unidad_investigacion',
            'competencia'] , axis = 1) #Se eliminan las columnas que  no son de utilidad

#print(df.columns)


df.drop(df[df['longitud'] == 'NA'].index, inplace = True)  #se borran los compos "NA" de la columna longitud pero se deja el espacio en blnaco

df = df[df['longitud'].notna()] #se eliminan las filas con el espacio en blnaco

#print(df.describe)


#Separacion de fecha en dia y hora

dfTime = df["fecha_hechos"].str.split('[/ ]', expand=True) #Se divide la cadena de texto de "fecha_hechos" 



dfTime = dfTime.rename(columns={0 :'dia_hechos', 3 :'hora_hechos'}) #Se cambia el numero que tiene de nombre por el nombre correcto

#dfTimeF = dfTime["fehca"] = dfTime[]  

dfTimeD = dfTime.drop([1,2] , axis=1)  #Se eliminan la columnas de datos de la fecha que no necesitamos


dfC= pd.concat([df ,dfTimeD], axis=1) #Se agreganlas dos columnas a la bae completa

dfC = dfC.drop(['fecha_hechos'] , axis=1)   #se elimina la columna de 'fecha_hehcos pues ya no es relevante

dfC = dfC[['dia_hechos', 'mes_hechos', 'ao_hechos', 'hora_hechos', 'delito', 'fiscalia', 'categoria_delito',
           'calle_hechos', 'calle_hechos2', 'colonia_hechos', 'alcaldia_hechos', 'longitud', 'latitud']]#Se hace un acomodo de las columnas por dia/mes/año


#Filtrar años de estudio

dfC.drop(dfC[dfC['ao_hechos'] <= 2015 ].index, inplace = True)  

dfC = dfC[dfC['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfC.drop(dfC[dfC['ao_hechos'] >= 2022 ].index, inplace = True)  

dfC = dfC[dfC['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

print(dfC.columns)

dfC.to_csv("D:\TT2\Data\BaseCompletaLimpia.csv", index=False) #guaramos el dataframe final en un CSV


#EDA


print(dfC.describe)

print(dfC.columns)

profile = ProfileReport(dfC, title="EDA Analisis de Crimen", explorative=True)

profile.to_file("ReporteEDA.html")

