import astropy
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import FK5
import pandas as pd

a = 0
df = []

while a >= -90:
    gc = SkyCoord(l=a*u.degree, b=0*u.degree, frame='galactic')
    icrs_coord = gc.transform_to(FK5(equinox='J2025.67'))
    ra_hms = icrs_coord.ra.to_string(unit=u.hour, sep=':', precision=2)
    dec = icrs_coord.dec.to_string(unit=u.deg, sep=':', precision = 2)
    print(str(dec))
    a = a-1
