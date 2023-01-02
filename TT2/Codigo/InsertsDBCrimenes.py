import pandas as pd
from sqlalchemy import create_engine
import pymysql

connection = pymysql.connect(host='localhost',
                             user='DataCriming',
                             password='DB1202',
                             db='Crimenes')


cursor = connection.cursor()

dfD = pd.read_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaDelito.csv")
dfF = pd.read_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaFecha.csv")
dfP = pd.read_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaPersona.csv")
dfU = pd.read_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaUbicacion.csv")
dfG = pd.read_csv("/home/ozkr/Documentos/GitHub/TTAnalisisDeCrimen/TT2/BaseCsv/TablaGeo.csv")


# creating column list for insertion
cols = "'Sexo','Edad','TipoPersona','CalidadJuridica'"

# Insert DataFrame recrds one by one.
for i,row in dfF.iterrows():
    sql = "INSERT INTO Fecha (`Dia`,`Mes`,`Año`,`Fecha`,`Hora`) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row) )

    connection.commit()

sqlSel = "SELECT * FROM `Fecha` limit 20"
cursor.execute(sqlSel)

result = cursor.fetchall()
for i in result:
    print(i)
    
    
connection.close()

