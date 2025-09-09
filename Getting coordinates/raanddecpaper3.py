import pandas as pd 
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u

data = ascii.read("paper3_table.txt")

df = data.to_pandas()

print(df.head())

df.to_csv("paper3_output.csv")
#df.to_csv("/Users/avery/Downloads/paper3_output.csv", index=False)