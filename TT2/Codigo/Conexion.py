import pandas as pd
from sqlalchemy import create_engine
import pymysql



connection = pymysql.connect(host='localhost',
                             user='DataCriming',
                             password='DB1202',
                             db='Crimenes')

cursor = connection.cursor()


sqlSel = "select * from Delito;"
cursor.execute(sqlSel)

result = cursor.fetchall()
for i in result:
    print(i)

connection.close()