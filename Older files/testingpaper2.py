from astroquery.simbad import Simbad
import pandas as pd
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u

exec(open("c:/Users/avery/Downloads/Young Worlds/testingpaper2.py").read())

# Initialize the Simbad query
simbad = Simbad()
simbad.add_votable_fields('ra', 'dec', 'ra_precision', 'dec_precision', 'otype', 'bibcodelist')

# Query all objects mentioned in the paper with the bibcode
bibcode = "2017A&A...598A..92L"
result = simbad.query_bibobj(bibcode)

# Convert to pandas DataFrame
df = result.to_pandas()
print(df.head())

# Save as CSV
df.to_csv("2017A&A-598A-92L_simbad_objects.csv", index=False)
