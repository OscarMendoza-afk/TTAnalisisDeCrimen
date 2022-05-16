import pandas as pd


df = pd.read_csv("..\..\..\DataSet\DatasetLimpia\VenustianoCarranzaLimpia.csv")



dfL = df.drop(['tempo'] , axis=1)

dfL.drop(dfL[dfL['longitud'] == 'NA'].index, inplace = True)

dfL = dfL[dfL['longitud'].notna()]

dfL.to_csv('..\DatasetLimpia\VenustianoCarranzaLimpia.csv', index=False)
