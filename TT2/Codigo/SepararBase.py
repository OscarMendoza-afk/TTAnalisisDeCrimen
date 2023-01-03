import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import math


df = pd.read_csv(r"/home/ozkr/Documentos/UpdateCrimenesENE.csv")

print(df.columns)

#df.rename(columns={'Alcalia': 'Alcaldia'}, inplace=True)

print(df.columns)

df = df.drop_duplicates(subset=['idCarpeta'])

def AddU(U):
    
    idU = 'U' + str(U)
    
    return idU


def AddP(P):
    
    idP = 'P' + str(P)
    
    return idP


def AddF(F):
    
    idF = 'F' + str(F)
    
    return idF



dfDelito = df[['Delito','Categoria','Competencia']]

dfDelito.to_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaDelito.csv", index=False)



dfUbicacion = df[['Alcaldia','Colonia']]

#dfUbicacion['idUbicacion'] = dfUbicacion.index

#dfUbicacion = dfUbicacion[['idUbicacion','Colonia','Alcaldia','longitud','latitud']]

#dfUbicacion['idUbicacion'] = dfUbicacion['idUbicacion'].apply(AddU)

dfUbicacion.to_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaUbicacion.csv", index=False)


dfGeo = df[['longitud','latitud']]

#dfUbicacion['idUbicacion'] = dfUbicacion.index

#dfUbicacion = dfUbicacion[['idUbicacion','Colonia','Alcaldia','longitud','latitud']]

#dfUbicacion['idUbicacion'] = dfUbicacion['idUbicacion'].apply(AddU)

dfGeo.to_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaGeo.csv", index=False)


dfPersona = df[['Sexo','Edad','TipoPersona','CalidadJuridica']]

#dfPersona['idPerosna'] = dfPersona.index

#dfPersona = dfPersona[['idPerosna','Sexo','Edad','TipoPersona']]

#dfPersona['idPerosna'] = dfPersona['idPerosna'].apply(AddP)

dfPersona.to_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaPersona.csv", index=False)



dfFecha= df[['Dia','Mes','Año','Fecha','Hora']]

#dfFecha['idFecha'] = dfFecha.index

#dfFecha = dfFecha[['idFecha','Dia','Mes','Año','Fecha','Hora']]

#dfFecha['idFecha'] = dfFecha['idFecha'].apply(AddF)

dfFecha.to_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaFecha.csv", index=False)

#print(dfFecha)

#dfDelito.duplicated(subset=['idCarpeta'])

print(df.describe)
