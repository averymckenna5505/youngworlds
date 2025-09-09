import pandas as pd

df = pd.read_csv("allcoords_unfiltered.csv")

for index, row in df.iterrows():
    rounded = round(row["RAdeg"],5)
    row["RAdeg"] = rounded
    roundeddec = round(row["DEdeg"],5)
    row["DEdeg"] = roundeddec

df.to_csv("/Users/avery/Downloads/allcoords_rounded2.csv", index=False)
df.to_csv("allcoords_rounded2.csv", index=False)