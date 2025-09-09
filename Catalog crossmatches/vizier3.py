from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
import time

# Read your star list (example assumes CSV with RA,Dec in degrees)
stars = pd.read_csv("test_vizier(Sheet1).csv")  
coords = SkyCoord(ra=stars["RA"].values*u.deg, dec=stars["Dec"].values*u.deg)

tic_catalog = "IV/38/tic82"       # TIC v8.2
wise_catalog = "II/328/allwise"   # AllWISE
search_radius = 5 * u.arcsec

Vizier.ROW_LIMIT = -1   # remove row limit
Vizier.TIMEOUT = 300    # allow long queries

def query_batch(catalog, coords, radius, prefix):
    """
    Query catalog for list of coords and return a DataFrame
    with each catalog column expanded and prefixed.
    """
    rows = []
    for i, c in enumerate(coords):
        try:
            r = Vizier.query_region(c, radius=radius, catalog=catalog)
            if r:
                row = r[0][0]   # closest match
            rows.append({f"{prefix}_{col}": row[col] for col in row.colnames})
            print(f"Star {i}: match found")
        else:
        except Exception as e:
            print(f"Error on star {i}: {e}")
            rows.append({})        
        time.sleep(0.1)  
        if i % 10 == 0:
            time.sleep(5)
        if i % 100 == 0:
            time.sleep(30)

    #df_rows = []
    #for row in rows:
    #    if row is None:
   #         df_rows.append({})
  #      else:
 #           df_rows.append({f"{prefix}_{col}": row[col] for col in row.colnames})
#    return pd.DataFrame(df_rows)
return pd.DataFrame(rows)

# Run queries and expand results
tic_df = query_batch(tic_catalog, coords, search_radius, prefix="TIC")
wise_df = query_batch(wise_catalog, coords, search_radius, prefix="WISE")

# Merge back with original star list
stars = pd.concat([stars, tic_df, wise_df], axis=1)

# Save
stars.to_pickle("crossmatch_results3.pkl")   # keeps full tables
stars.to_csv("crossmatch_summary3.csv", index=False)  # expanded summary