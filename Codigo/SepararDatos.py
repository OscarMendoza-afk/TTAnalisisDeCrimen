import pandas as pd


df = pd.read_csv("..\..\..\DataSet\DatasetLimpia\VenustianoCarranzaLimpia.csv")

#print(df)


dfL = df["fecha_hechos"].str.split('[/ ]', expand=True)

dfL = dfL.rename(columns={0 :'dia_hechos', 3 :'hora_hechos'})

dfL = dfL.drop([1,2] , axis=1)

print(dfL)

dfS= pd.concat([df ,dfL], axis=1)

print(dfS.columns)

dfS.to_csv('..\..\..\DataSet\FechaSeparada\VenustianoCarranzaSeparada.csv', index=False)
