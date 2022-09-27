import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


df = pd.read_csv(r"D:\TT2\Data\UpdateCrimenes.csv" )   #Se carga el archivo CSV como un dataframe

print(df.columns)


df = df.drop([
             
            'Año_inicio', 
            'Mes_inicio', 
            'FechaInicio',
            'HoraInicio',
            'competencia'] , axis = 1) #Se eliminan las columnas que  no son de utilidad

#print(df.columns)


df.drop(df[df['longitud'] == 'NA'].index, inplace = True)  #se borran los compos "NA" de la columna longitud pero se deja el espacio en blnaco

df = df[df['longitud'].notna()] #se eliminan las filas con el espacio en blnaco

#print(df.describe)


#Separacion de fecha en dia y hora

dfT = df["FechaHecho"].str.split('[/ ]', expand=True) #Se divide la cadena de texto de "fecha_hechos" 



dfT = dfT.rename(columns={1 :'dia_hechos', 3 :'hora_hechos'}) #Se cambia el numero que tiene de nombre por el nombre correcto


dfT = dfT.drop([0,2] , axis=1)  #Se eliminan la columnas de datos de la fecha que no necesitamos


dfS= pd.concat([df ,dfT], axis=1) #Se agreganlas dos columnas a la bae completa

dfS = dfS.drop(['FechaHecho'] , axis=1)   #se elimina la columna de 'fecha_hehcos pues ya no es relevante

dfS = dfS[['dia_hechos', 'Mes_hecho', 'Año_hecho', 'HoraHecho', 'Delito', 'CalidadJuridica', 'Categoria', 'ColoniaHechos', 'AlcaldiaHechos', 'longitud', 'latitud']]#Se hace un acomodo de las columnas por dia/mes/año


#Filtrar años de estudio

dfS.drop(dfS[dfS['Año_hecho'] <= 2015 ].index, inplace = True)  

dfS = dfS[dfS['Año_hecho'].notna()] #se eliminan las filas con el espacio en blnaco

dfS.drop(dfS[dfS['Año_hecho'] >= 2022 ].index, inplace = True)  

dfS = dfS[dfS['Año_hecho'].notna()] #se eliminan las filas con el espacio en blnaco

print(dfS.columns)

dfS.to_csv("D:\TT2\Data\BaseCompletaLimpia.csv", index=False) #guaramos el dataframe final en un CSV


#EDA


print(dfS.describe)

print(dfS.columns)

#profile = ProfileReport(dfS, title="EDA Analisis de Crimen", explorative=True)

#profile.to_file("ReporteEDAUpdate.html")