import numpy as np
from astroquery.gaia import Gaia
from astropy.table import Table
from itertools import chain
import pandas
import astropy.units as u


try:
    Gaia.login()
    print("Successfully logged into Gaia archive.")
except Exception as e:
    print(f"Gaia login failed. Please ensure your credentials are set up correctly. Error: {e}")

#df = pandas.read_csv("cleaned_coordinates2.csv")
#astro_table = Table.from_pandas(df)
#upload_table_name = "my_input_coords"

#try:
#    Gaia.upload_table(upload_resource=astro_table, table_name=upload_table_name)
#    print(f"Table '{upload_table_name}' uploaded successfully to Gaia archive.")
#except Exception as e:
#    print(f"Failed to upload table '{upload_table_name}'. Error: {e}")
#    exit()

radius_arcsec = 5
query = f"""
SELECT 
  my_input_coords.ra AS input_ra,
  my_input_coords.dec AS input_dec,
  gaia.source_id,
  gaia.ra,
  gaia.dec,
  gaia.parallax,
  gaia.bp_rp,
  gaia.phot_g_mean_mag,
  gaia.ruwe,
  1e3 * DISTANCE(
    POINT(my_input_coords.ra, my_input_coords.dec),
    POINT(gaia.ra, gaia.dec)
  ) AS separation_mas
FROM 
  user_awalters.my_input_coords AS my_input_coords
JOIN 
  gaiadr3.gaia_source AS gaia
ON 
  1=CONTAINS(
    POINT(gaia.ra, gaia.dec),
    CIRCLE(my_input_coords.ra, my_input_coords.dec, {radius_arcsec/3600.0})
  )
"""
print("\nExecuting ADQL Query:")

try:
    job = Gaia.launch_job_async(query)
    print(f"Gaia query job ID: {job.jobid}")
    results = job.get_results()
    print("Query completed successfully.")
except Exception as e:
    print(f"Failed to execute Gaia query. Error: {e}")
    exit()

results.write("gaia_bulk_crossmatch_results.csv", format="csv", overwrite=True)
print(results[:5])