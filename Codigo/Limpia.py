import numpy as np
import pandas as pd

dataset = pd.read_csv("Iztacalco.csv")

print(dataset)

#filtro = dataset['longitud'] != "NA"
#iztacalcoLimpia = dataset[filtro]

#iztacalcoLimpia.head()