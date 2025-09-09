import pandas as pd 
import numpy as np
from astropy.io import ascii

# Load the MRT file
data = ascii.read("/Users/avery/Downloads/starcatalog1.txt",format='cds')

df = data.to_pandas()

print(df.columns)
print(df.head)

filtered = df[(df["FeH"] < -0.5) & 
              (df["Teff"] > 2500) & (df["Teff"] < 5000) &
              (df["logg"] > 4.5)]

filtered.to_csv("/Users/avery/Downloads/filteredstarcatalog1.csv", index=False)

#data1 = data["ID"]
#print(data1.head())
#selected_data1 = data['ID', 'parallax','Bp-Rp','ruwe', 'FeH']


# View the column names to identify what you need

#file_path = r"C:\Users\avery\Downloads\starcatalog1.txt"

#average_ruwe = data["ruwe"].mean()

#print(average_ruwe)
#df = pd.read_csv(file_path, skiprows=60)  # You may need to adjust this

#print(df.iloc[0,2])
