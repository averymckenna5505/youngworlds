from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
import time

stars = pd.read_csv("combined_highmetal8_28.csv")  
coords = SkyCoord(ra=stars["ra"].values*u.deg, dec=stars["dec"].values*u.deg)

tic_catalog = "IV/38/tic82"
wise_catalog = "II/328/allwise"
twomass_catalog = "II/246/out"
search_radius = 5 * u.arcsec

Vizier.ROW_LIMIT = -1
Vizier.TIMEOUT = 650

def query_batch(catalog, coords, radius, prefix):
    df_rows = []
    for i, c in enumerate(coords):
        try:
            r = Vizier.query_region(c, radius=radius, catalog=catalog)
            if r:
                row = r[0][0] 
                df_rows.append({f"{prefix}_{col}": row[col] for col in row.colnames})
                print(f"Star {i}: match found")
            else:
                df_rows.append({}) 
                print(f"Star {i}: no match")
        except Exception as e:
            print(f"Error on star {i}: {e}")
            df_rows.append({})

        time.sleep(0.1)  
        if i > 0 and i % 10 == 0:
            time.sleep(5)
        if i > 0 and i % 100 == 0:
            time.sleep(30)

    return pd.DataFrame(df_rows)

#tic_df = query_batch(tic_catalog, coords, search_radius, prefix="TIC")
#wise_df = query_batch(wise_catalog, coords, search_radius, prefix="WISE")
twomass_df = query_batch(twomass_catalog, coords, search_radius, prefix="2MASS")

stars = pd.concat([stars, twomass_df], axis=1)

#stars.to_pickle("crossmatch_results3.pkl") 
stars.to_csv("crossmatch_summaryhigh.csv", index=False) 