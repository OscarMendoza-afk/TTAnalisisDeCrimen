import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport



df = pd.read_csv(r"C:\Users\ozkr_\Downloads\BaseLimpiaUpdate.csv" )

print(df.Alcalia)

df['Alcalia'].unique()


for Alcalia in df['Alcalia'].unique():

    # Select data for the distrito
    datos_area = df[df.Alcalia == Alcalia]

    # Write the new DataFrame to a CSV file
    filename = str(Alcalia) + '.csv'
    datos_area.to_csv(filename)