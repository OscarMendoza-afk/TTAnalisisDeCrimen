import pandas as pd
from sqlalchemy import create_engine
import pymysql

usuario = 'DataCriming'
contrasena = 'DB1202'
url_servidor = 'localhost'
puerto = '3306'
esquema = 'Crimenes'
plugin_autenticacion = 'mysql_native_password'


c_conexion = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}?auth_plugin={5}'
c_conexion = c_conexion.format(usuario, contrasena, url_servidor, puerto,
                               esquema, plugin_autenticacion)
motor_mysql_mariadb = create_engine(c_conexion)

consulta_sqlD = '''
SELECT
  *
FROM Delito
'''

consulta_sqlP = '''
SELECT
  *
FROM Persona
'''


consulta_sqlU = '''
SELECT
  *
FROM Ubicacion
'''


consulta_sqlF = '''
SELECT
  *
FROM Fecha
'''




dfDelito = pd.read_sql_query(
        consulta_sqlD, motor_mysql_mariadb)


dfPersona = pd.read_sql_query(
        consulta_sqlP, motor_mysql_mariadb)

dfUbicacion = pd.read_sql_query(
        consulta_sqlU, motor_mysql_mariadb)

dfFecha = pd.read_sql_query(
        consulta_sqlF, motor_mysql_mariadb)


print(dfDelito.columns)
