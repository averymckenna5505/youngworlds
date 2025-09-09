import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

df = pd.read_csv("paper2_usedcoordinates(in).csv")

coords = SkyCoord(ra=df["RA"], dec=df["DEC"], unit=(u.hourangle, u.deg))

df["RAdeg"] = coords.ra.deg
df["DEdeg"] = coords.dec.deg

#df.to_csv("paper2_usedcoordinates(out).csv", index=False)
df.to_csv("/Users/avery/Downloads/paper2_usedcoordinated(deg).csv", index=False)
