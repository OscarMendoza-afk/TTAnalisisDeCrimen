import numpy as np
import pandas as pd

df = pd.read_csv("..\DatasetOriginal\CuauhtemocUTF.csv")



dfL = df.drop(['tempo'] , axis=1)


#filtro = dfL[dfL['longitud'] == "NA"].index

dfL.drop(dfL[dfL['longitud'] == 'NA'].index, inplace = True)


#iztacalcoLimpia.head()

#iztacalcoLimpia.to_csv('IztacalcoLimpia.csv', index=False)

#dfL = df.drop(df[df['longitud'] == "NA"].index)
dfL = dfL[dfL['longitud'].notna()]

dfL.to_csv('..\DatasetLimpia\CuauhtemocLimpia.csv', index=False)



