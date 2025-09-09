import pandas as pd

df = pd.read_csv("paper5table.txt", delim_whitespace=True)

df.to_csv("paper5_output.csv", index=False)
#df.to_csv("/Users/avery/Downloads/paper5_output.csv", index=False)