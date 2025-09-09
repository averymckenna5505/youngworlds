import pandas as pd 
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.table import Table

file_path = 'aj269741t2_ascii.txt'

try:
    data = ascii.read(file_path)
    print("Successfully read the table.")
    print("Column names:")
    for col in data.colnames:
        print(f" - {col}")
except Exception as e:
    print("Error reading file:", e)