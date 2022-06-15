import pandas as pd


#Limpieza de columnas y datos vacios


df = pd.read_csv("..\..\..\DataSet\DataBase.csv" )   #Se carga el archivo CSV como un dataframe

print(df.columns)


dfL = df.drop([
            'tempo', 
            'ao_inicio', 
            'mes_inicio', 
            'fecha_inicio', 
            'agencia', 
            'unidad_investigacion',
            'competencia'] , axis=1) #Se eliminan las columnas que  no son de utilidad

dfL.drop(dfL[dfL['longitud'] == 'NA'].index, inplace = True)  #se borran los compos "NA" de la columna longitud pero se deja el espacio en blnaco

dfL = dfL[df['longitud'].notna()] #se eliminan las filas con el espacio en blnaco


#Separacion de fecha en dia y hora

dfT = dfL["fecha_hechos"].str.split('[- ]', expand=True) #Se divide la cadena de texto de "fecha_hechos" 


dfT = dfT.rename(columns={1 :'dia_hechos', 3 :'hora_hechos'}) #Se cambia el numero que tiene de nombre por el nombre correcto


dfT = dfT.drop([0,2] , axis=1)  #Se eliminan la columnas de datos de la fecha que no necesitamos




dfS= pd.concat([dfL ,dfT], axis=1) #Se agreganlas dos columnas a la bae completa

dfS = dfS.drop(['fecha_hechos'] , axis=1)   #se elimina la columna de 'fecha_hehcos pues ya no es relevante

dfS = dfS[['dia_hechos', 'mes_hechos', 'ao_hechos', 'hora_hechos', 'delito', 'fiscalia', 'categoria_delito',
           'calle_hechos', 'calle_hechos2', 'colonia_hechos', 'alcaldia_hechos', 'longitud', 'latitud']]#Se hace un acomodo de las columnas por dia/mes/año

print(dfS)


dfS.drop(dfS[dfS['ao_hechos'] <= 2015 ].index, inplace = True)  

dfS = dfS[dfS['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfS.drop(dfS[dfS['ao_hechos'] >= 2022 ].index, inplace = True)  

dfS = dfS[dfS['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco



#Filtar alcaldias de estuido

dfA = dfS.copy()


dfIZTAPALAPA= dfA.copy()
dfIZTAPALAPA.drop(dfIZTAPALAPA[dfIZTAPALAPA['alcaldia_hechos'] != 'IZTAPALAPA'].index, inplace = True)  #filtramos las alcaldias por iztapalapa
dfIZTAPALAPA = dfIZTAPALAPA[dfIZTAPALAPA['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfGUSTAVOAMADER = dfA.copy()
dfGUSTAVOAMADER.drop(dfGUSTAVOAMADER [dfGUSTAVOAMADER ['alcaldia_hechos'] != 'GUSTAVO A MADERO'].index, inplace = True)  #filtramos las alcaldias por Gustavo A Madero
dfGUSTAVOAMADER = dfGUSTAVOAMADER [dfGUSTAVOAMADER ['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfAZCAPOTZALCO = dfA.copy()
dfAZCAPOTZALCO.drop(dfAZCAPOTZALCO [dfAZCAPOTZALCO ['alcaldia_hechos'] != 'AZCAPOTZALCO'].index, inplace = True)  #filtramos las alcaldias por Azcapotzalco
dfAZCAPOTZALCO = dfAZCAPOTZALCO [dfAZCAPOTZALCO ['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfVENUSTIANOCARRANZA = dfA.copy()
dfVENUSTIANOCARRANZA.drop(dfVENUSTIANOCARRANZA [dfVENUSTIANOCARRANZA ['alcaldia_hechos'] != 'VENUSTIANO CARRANZA'].index, inplace = True)  #filtramos las alcaldias por Venustiano Carranza
dfVENUSTIANOCARRANZA = dfVENUSTIANOCARRANZA [dfVENUSTIANOCARRANZA ['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfCUAUHTEMOC = dfA.copy()
dfCUAUHTEMOC.drop(dfCUAUHTEMOC [dfCUAUHTEMOC ['alcaldia_hechos'] != 'CUAUHTEMOC'].index, inplace = True)  #filtramos las alcaldias por Cuauhtemoc
dfCUAUHTEMOC = dfCUAUHTEMOC [dfCUAUHTEMOC ['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfIZTACALCO = dfA.copy()
dfIZTACALCO.drop(dfIZTACALCO [dfIZTACALCO ['alcaldia_hechos'] != 'IZTACALCO'].index, inplace = True)  #filtramos las alcaldias por Iztacalco
dfIZTACALCO = dfIZTACALCO [dfIZTACALCO ['alcaldia_hechos'].notna()] #se eliminan las filas con el espacio en blnaco


dfIZTAPALAPA.to_csv('..\..\..\DataSet\FechaSeparada\dfIZTAPALAPA.csv', index=False)
dfGUSTAVOAMADER.to_csv('..\..\..\DataSet\FechaSeparada\dfGUSTAVOAMADER.csv', index=False)
dfAZCAPOTZALCO.to_csv('..\..\..\DataSet\FechaSeparada\dfAZCAPOTZALCO.csv', index=False)
dfVENUSTIANOCARRANZA.to_csv('..\..\..\DataSet\FechaSeparada\dfVENUSTIANOCARRANZA.csv', index=False)
dfCUAUHTEMOC.to_csv('..\..\..\DataSet\FechaSeparada\dfCUAUHTEMOC.csv', index=False)
dfIZTACALCO.to_csv('..\..\..\DataSet\FechaSeparada\dfIZTACALCO.csv', index=False)


dfFinal = pd.concat([dfIZTAPALAPA,dfGUSTAVOAMADER,dfAZCAPOTZALCO,dfVENUSTIANOCARRANZA,dfCUAUHTEMOC,dfIZTACALCO]) #Concatenamos todas las bases de la alcaldia en una sola

"""

dfFinal.drop(dfFinal[dfFinal['ao_hechos'] <= 2015 ].index, inplace = True)  

dfFinal = dfFinal[dfFinal['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

dfFinal.drop(dfFinal[dfFinal['ao_hechos'] >= 2022 ].index, inplace = True)  

dfFinal = dfFinal[dfFinal['ao_hechos'].notna()] #se eliminan las filas con el espacio en blnaco

"""


dfFinal.to_csv('..\..\..\DataSet\FechaSeparada\BaseCompletaLimpia.csv', index=False) #guaramos el dataframe final en un CSV



print(dfFinal.columns)




print(dfFinal['ao_hechos'].value_counts(dropna=False).head(10))
print(df['ao_hechos'].value_counts(dropna=False).head(10))
