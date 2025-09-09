import pandas as pd
from astropy.coordinates import SkyCoord
from astropy import units as u

# --- Settings ---
file1 = 'combined_unique_stars123_4.csv'  # first input file
file2 = 'paper5_usedcoordinates(out).csv'  # second input file
tolerance_arcsec = 5  # arcsecond threshold for matching

# --- Load data ---
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# --- Convert to SkyCoord objects ---
coords1 = SkyCoord(ra=df1['RAdeg'].values * u.deg, dec=df1['DEdeg'].values * u.deg)
coords2 = SkyCoord(ra=df2['RAdeg'].values * u.deg, dec=df2['DEdeg'].values * u.deg)

# --- Match coords2 against coords1 ---
idx, d2d, _ = coords2.match_to_catalog_sky(coords1)

# --- Filter out stars in df2 that are within tolerance of any star in df1 ---
mask_far = d2d > tolerance_arcsec * u.arcsec
df2_unique = df2[mask_far].reset_index(drop=True)

# --- Combine unique stars from both files ---
combined_df = pd.concat([df1, df2_unique], ignore_index=True)

# --- Save result ---
combined_df.to_csv('combined_unique_stars1234_5.csv', index=False)

print(f"Combined catalog saved with {len(combined_df)} unique stars.")