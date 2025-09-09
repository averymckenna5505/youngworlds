from astropy.io import fits
import pandas as pd
from astropy.table import Table

table = Table.read("paper4table.fits")

table.write("paper4_output.csv", format="csv", overwrite=True)
#table.write("/Users/avery/Downloads/paper4_output.csv", format="csv", overwrite=True)
