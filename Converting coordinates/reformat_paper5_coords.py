import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

df = pd.read_csv("paper5_usedcoordinates(in).csv")

for index, row in df.iterrows():
    if row["RaH"] < 10:
        RaH = "0"+str(int(row["RaH"]))
    else:
        RaH = str(int(row["RaH"]))
    if row["RaM"] < 10:
        RaM = "0"+str(int(row["RaM"]))
    else:
        RaM = str(int(row["RaM"]))
    if row["RaS"] < 10:
        RaS = "0"+str(row["RaS"])
    else:
        RaS = str(row["RaS"])

    if row["Dec deg"] > 0:
        DecD = "+"+str(int(row["Dec deg"]))
    else:
        DecD = str(int(row["Dec deg"]))
    if row["DecM"] < 10:
        DecM = "0"+str(int(row["DecM"]))
    else:
        DecM = str(int(row["DecM"]))
    if row["DecS"] < 10:
        DecS = "0"+str(row["DecS"])
    else:
        DecS = str(row["DecS"])

    ra_result = RaH+" "+RaM+" "+RaS

    dec_result = DecD+" "+DecM+" "+DecS

    df.at[index, "RA"] = ra_result
    df.at[index, "DEC"] = dec_result

df.to_csv("/Users/avery/Downloads/paper5_usedcoordinates(mid).csv", index=False)
df.to_csv("paper5_usedcoordinates(mid).csv", index=False)

