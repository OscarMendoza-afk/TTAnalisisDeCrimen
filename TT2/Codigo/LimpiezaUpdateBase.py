import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

#Limpieza de columnas y datos vacios


#Se carga el archivo CSV como un dataframe

dfU = pd.read_csv(r"/home/ozkr/Documentos/BasesLimpias/CrimenesCleanSDF.csv")

print(dfU.columns)
print(dfU.head)

print(dfU["HoraHecho"])

dfU = dfU.drop([
            
            'Año_inicio', 
            'Mes_inicio', 
            'FechaInicio',
            'HoraInicio'] , axis = 1) #Se eliminan las columnas que  no son de utilidad

print(dfU.columns)


dfU.drop(dfU[dfU['longitud'] == 'NA'].index, inplace = True)  #se borran los compos "NA" de la columna longitud pero se deja el espacio en blnaco

dfU = dfU[dfU['longitud'].notna()] #se eliminan las filas con el espacio en blnaco




#Separacion de fecha en dia y hora

dfT = dfU["FechaHecho"].str.split('[/ ]', expand=True) #Se divide la cadena de texto de "fecha_hechos" 



dfT = dfT.rename(columns={1 :'dia_hechos', 3 :'hora_hechos'}) #Se cambia el numero que tiene de nombre por el nombre correcto


dfT = dfT.drop([0,2] , axis=1)  #Se eliminan la columnas de datos de la fecha que no necesitamos


dfS= pd.concat([dfU ,dfT], axis=1) #Se agreganlas dos columnas a la bae completa

#dfS = dfS.drop(['FechaHecho'] , axis=1)   #se elimina la columna de 'fecha_hehcos pues ya no es relevante

dfS = dfS[[
           'idCarpeta',
           'dia_hechos', 
           'Mes_hecho', 
           'Año_hecho',
           'FechaHecho',
           'HoraHecho', 
           'Delito', 
           'CalidadJuridica', 
           'Categoria', 
           'competencia',
           'ColoniaHechos', 
           'AlcaldiaHechos',
           'Sexo',
           'Edad',
           'TipoPersona',
           'longitud', 
           'latitud']]#Se hace un acomodo de las columnas por dia/mes/año


#Filtrar años de estudio

dfS.drop(dfS[dfS['Año_hecho'] <= 2015 ].index, inplace = True)  

#dfS = dfS[dfS['Año_hecho'].notna()] #se eliminan las filas con el espacio en blnaco

dfS.drop(dfS[dfS['Año_hecho'] >= 2023 ].index, inplace = True)  

#dfS = dfS[dfS['Año_hecho'].notna()] #se eliminan las filas con el espacio en blnaco

#print(dfS.columns)


dfS = dfS.rename(columns={'dia_hechos' :'Dia', 'competencia' : 'Competencia', 'Mes_hecho' :'Mes', 'Año_hecho' : 'Año' , 'FechaHecho': 'Fecha', 'HoraHecho' : 'Hora', 'ColoniaHechos' : 'Colonia', 'AlcaldiaHechos' : 'Alcaldia', })
print(dfS.columns)
#EDA

dfS.to_csv("/home/ozkr/Documentos/UpdateCrimenesENE.csv", index=False) #guaramos el dataframe final en un CSV

#print(dfS.head)

print(dfS.head)

#profile = ProfileReport(dfS, title="EDA Update", explorative=True)

#profile.to_file("ReporteEDA1ENE.html")