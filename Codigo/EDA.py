import numpy as np
import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

df = pd.read_csv(r"C:\Users\ozkr_\Documents\TT\DataSet\BaseCompletaLimpia.csv")

print(df.describe)



profile = ProfileReport(df, title="EDA Analisis de Crimen", explorative=True)

profile.to_file("ReporteEDA.html")

