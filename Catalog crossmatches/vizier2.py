from astroquery.xmatch import XMatch
import astropy.units as u
import pandas as pd

# --- Load your star list ---
# Your CSV should have at least: RA, Dec
stars = pd.read_csv("cut_star_list(in).csv")  

# --- Define catalogs ---
tic_catalog = "vizier:IV/38/tic82"        # TIC v8.2
wise_catalog = "vizier:II/328/allwise"    # AllWISE

# --- Match radius ---
search_radius = 5 * u.arcsec   # adjust if needed

# --- Crossmatch with TIC ---
print("Crossmatching with TIC...")
tic_results = XMatch.query(
    cat1=stars,
    cat2=tic_catalog,
    max_distance=search_radius,
    colRA1="RA", colDec1="Dec"
)

# --- Crossmatch with AllWISE ---
print("Crossmatching with AllWISE...")
wise_results = XMatch.query(
    cat1=stars,
    cat2=wise_catalog,
    max_distance=search_radius,
    colRA1="RA", colDec1="Dec"
)

# --- Save results ---
tic_results.write("tic_crossmatch.csv", format="csv", overwrite=True)
wise_results.write("wise_crossmatch.csv", format="csv", overwrite=True)

print("Done! Results saved as tic_crossmatch.csv and wise_crossmatch.csv")