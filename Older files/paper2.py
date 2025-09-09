import pandas as pd 
import numpy as np
from astropy.io import ascii
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy import units as u

df = pd.read_csv("/Users/avery/Downloads/mypaper1data.txt", delim_whitespace=True, skiprows=2)

print(df.head)

#data1 = ascii.read("/Users/avery/Downloads/paper2data1.txt", 
   #                format='basic', 
  #                 guess=False, 
 #                  fast_reader=False)
#data2 = ascii.read("/Users/avery/Downloads/paper2data2.txt", 
    #               format='basic', 
     #              guess=False, 
      #             fast_reader=False)


#df1 = data1.to_pandas()
#df2 = data2.to_pandas()

#merged = pd.merge(df2, df1, on="Object", how="left")

#merged['R.A.'] = merged['R.A.'].astype(str).str.replace(r'[^\x00-\x7F]+', ' ', regex=True).str.strip()
#merged['Decl.'] = merged['Decl.'].astype(str).str.replace(r'[^\x00-\x7F]+', ' ', regex=True).str.strip()

# Drop missing coordinates
#merged = merged.dropna(subset=['R.A.', 'Decl.'])

# Combine into coordinate strings
#merged['coord_str'] = merged['R.A.'] + ' ' + merged['Decl.']

# Convert to SkyCoord
#coords = SkyCoord(merged['coord_str'].values, unit=(u.hourangle, u.deg))

# Add decimal degree columns
#merged['RA_deg'] = coords.ra.deg
#merged['Dec_deg'] = coords.dec.deg

#print(merged.head)


#merged['coord_str'] = merged['R.A.'].astype(str).str.strip() + ' ' + merged['Decl.'].astype(str).str.strip()

#coords = SkyCoord(merged['coord_str'].values, unit=(u.hourangle, u.deg))

#merged['RA_deg'] = coords.ra.deg
#merged['Dec_deg'] = coords.dec.deg

#print(merged[['Object', 'R.A.', 'Decl.', 'RA_deg', 'Dec_deg']].head())

#filtered = df[(df["FeH"] < -0.5) & 
 #             (df["Teff"] > 2500) & (df["Teff"] < 5000) &
  #            (df["logg"] > 4.5)]

#filtered.to_csv("/Users/avery/Downloads/DTF2.csv", index=False)
