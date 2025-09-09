import numpy as np
from astropy.io import fits
from scipy.io import readsav
from astropy.io import ascii
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

#compares coordinates from paper 1 and paper 2

source1 = readsav('paper1_usedcoordinates.csv',verbose=1)
source2 = pd.read_csv("paper2_usedcoordinates(out).csv")

max_sep = 5*u.arcsec

catalog = SkyCoord(ra=float(source1[0])*u.degree,dec=float(source1[1])*u.degree)
c = SkyCoord(ra=float(source2[2])*u.degree,dec=float(source2[3])*u.degree)

idx, d2d, d3d = c.match_to_catalog_sky(catalog)  
sep_constraint = d2d < max_sep
bad = d2d > max_sep
c_matches = c[sep_constraint] 
catalog_matches = catalog[idx[sep_constraint]]

plt.hist(d2d.arcsec,bins=20)
plt.xlabel('Separation between object and best-match in arcseconds')
plt.show()

plt.hist(d2d[sep_constraint].arcsec,bins=20)
plt.show()

