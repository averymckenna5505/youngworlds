import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("crossmatch_summary3(Sheet1).csv")
df2 = pd.read_csv("crossmatch_summaryhigh.csv")

plt.scatter(df2['2MASS_Hmag']-df2['2MASS_Kmag'], df2['2MASS_Jmag']-df2['2MASS_Kmag'], s=0.4,color='red', alpha = 0.5, label='High Metallicity')
plt.scatter(df['2MASS_Hmag']-df['2MASS_Kmag'], df['2MASS_Jmag']-df['2MASS_Kmag'], s=0.6,color='blue', alpha = 0.9, label='Low Metallicity')
plt.xlabel('H-K') 
plt.ylabel('J-K') 
plt.ylim(0.7,1.1)
plt.xlim(-0.3,0.6)
plt.title('J-K vs. H-K') 
#plt.gca().invert_yaxis()
plt.grid(True)
plt.show()