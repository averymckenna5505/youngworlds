import pandas as pd 
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u

data = ascii.read("/Users/avery/Downloads/starcatalog1.txt",format='cds')

df = data.to_pandas()

print(df.columns())
print(df.head())

df["SpT"] = "M"+df["SpT"].astype(str)

filtered = df[(df["FeH"] < -0.5) & 
              (df["Teff"] > 2500) & (df["Teff"] < 5000) &
              (df["logg"] > 4.5)]

filtered.to_csv("/Users/avery/Downloads/DTF2.csv", index=False)
