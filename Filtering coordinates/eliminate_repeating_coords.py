import pandas as pd
import numpy as np

df = pd.read_csv("allcoords_rounded2.csv")

df_unique = df.drop_duplicates()

df_unique.to_csv("cleaned_coordinates2.csv", index=False)
df_unique.to_csv("/Users/avery/Downloads/cleaned_coordinates2.csv", index=False)
