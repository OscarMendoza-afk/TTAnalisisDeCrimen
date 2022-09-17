import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport

df = pd.read_csv(r"D:\Windows11Save2\Docs\TT\DataSet\BaseCompletaLimpia.csv")

print(df.describe)



profile = ProfileReport(df, title="EDA Analisis de Crimen", explorative=True)

profile.to_file("ReporteEDA.html")

