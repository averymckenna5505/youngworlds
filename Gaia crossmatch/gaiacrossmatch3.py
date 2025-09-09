import numpy as np
from astroquery.gaia import Gaia
from astropy.table import Table
import pandas

# Login to Gaia
try:
    Gaia.login()
    print("Successfully logged into Gaia archive.")
except Exception as e:
    print(f"Gaia login failed. Please ensure your credentials are set up correctly. Error: {e}")

# Load your coordinates
df = pandas.read_csv("final_clean_stars.csv")
astro_table = Table.from_pandas(df)
upload_table_name = "my_input_coords_new2"

# Upload table
try:
    Gaia.upload_table(upload_resource=astro_table, table_name=upload_table_name)
    print(f"Table '{upload_table_name}' uploaded successfully to Gaia archive.")
except Exception as e:
    print(f"Failed to upload table '{upload_table_name}'. Error: {e}")
    exit()
radius_arcsec = 2
radius_deg = radius_arcsec / 3600.0

# Fixed ADQL query
query = f"""
SELECT
    my_input_coords_new2.ra AS input_ra,
    my_input_coords_new2.dec AS input_dec,
    gaia.source_id,
    gaia.ra,
    gaia.dec,
    gaia.parallax,
    gaia.bp_rp,
    gaia.phot_g_mean_mag,
    gaia.ruwe,
    1e3 * DISTANCE(
        POINT('ICRS', my_input_coords_new2.ra, my_input_coords_new2.dec),
        POINT('ICRS', gaia.ra, gaia.dec)
    ) AS separation_mas
FROM
    user_awalters.my_input_coords_new2 AS my_input_coords_new2
JOIN
    gaiadr3.gaia_source AS gaia
ON
    CONTAINS(
        POINT('ICRS', gaia.ra, gaia.dec),
        CIRCLE('ICRS', my_input_coords_new2.ra, my_input_coords_new2.dec, {radius_deg})
    ) = 1
"""
print("\nExecuting ADQL Query:")

# Run query
try:
    job = Gaia.launch_job_async(query)
    print(f"Gaia query job ID: {job.jobid}")
    results = job.get_results()
    print("Query completed successfully.")
except Exception as e:
    print(f"Failed to execute Gaia query. Error: {e}")
    exit()

# Save results
results.write("gaia_bulk_crossmatch_results.csv", format="csv", overwrite=True)
print(results[:5])