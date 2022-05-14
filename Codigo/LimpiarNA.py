import pandas as pd

alcaldia= "" +

df = pd.read_csv("..\DatasetOriginal\VenustianoCarranzaUTF.csv")



dfL = df.drop(['tempo'] , axis=1)

dfL.drop(dfL[dfL['longitud'] == 'NA'].index, inplace = True)

dfL = dfL[dfL['longitud'].notna()]

dfL.to_csv('..\DatasetLimpia\VenustianoCarranzaLimpia.csv', index=False)

