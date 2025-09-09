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

def query_batch(catalog, coords, radius):
    results = []
    for i, c in enumerate(coords):
        try:
            r = Vizier.query_region(c, radius=radius, catalog=catalog)
            if r:  # if any result returned
                row = r[0][0]   # take closest match
                results.append(row)
                print(f"Star {i}")
            else:
                results.append(None)
        except Exception as e:
            print(f"Error on star {i}: {e}")
            results.append(None)
        time.sleep(0.1)  # small delay to avoid hammering Vizier
        if i%10 == 0:
            time.sleep(5)
        if i%100 == 0:
            time.sleep(30)
    return results

# Run queries
tic_matches = query_batch(tic_catalog, coords, search_radius)
wise_matches = query_batch(wise_catalog, coords, search_radius)

# Merge back into your dataframe
stars["TIC_match"] = tic_matches
stars["WISE_match"] = wise_matches

# Save
stars.to_pickle("crossmatch_results1.pkl")   # keeps full tables
stars.to_csv("crossmatch_summary1.csv")      # lighter summary