import pandas as pd 
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u

data = ascii.read("/Users/avery/Downloads/asciipracice.txt")

df = data.to_pandas()

print(df.columns)
print(df.head())

#def ra_hms_to_deg(h, m, s):
#    return 15 * (h + (m/60) + (s/3600))

#df["RAdeg"] = ra_hms_to_deg(df["RAh"], df["RAm"], df["RAs"])


#oordinates = df[["DEd", "RAdeg"]]

#coordinates.to_csv("/Users/avery/Downloads/paper2coordinates.csv", index=False)
