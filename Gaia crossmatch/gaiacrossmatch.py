from astroquery.gaia import Gaia
import pandas as pd
from astropy.table import Table
import astropy.units as u

df = pd.read_csv("cleaned_coordinates.csv")

astro_table = Table.from_pandas(df)
upload_table_name = "coordinate_table"
Gaia.login() 
Gaia.upload_table(upload_resource=astro_table, table_name=upload_table_name, format='csv')

radius_arcsec = 5
query = f"""
SELECT 
  gaia.source_id,
  gaia.ra,
  gaia.dec,
  gaia.parallax,
  gaia.bp_rp,
  gaia.phot_g_mean_mag
  user_table.ra AS input_ra,
  user_table.dec AS input_dec
FROM 
  user:{upload_table_name} AS user_table
JOIN 
  gaiadr3.gaia_source AS gaia
ON 
  1=CONTAINS(
    POINT('ICRS', gaia.ra, gaia.dec),
    CIRCLE('ICRS', user_table.ra, user_table.dec, {radius_arcsec/3600.0})
  )
"""

job = Gaia.launch_job_async(query)
results = job.get_results()

results.write("gaia_bulk_crossmatch_results.csv", format="csv", overwrite=True)
print(results[:5])