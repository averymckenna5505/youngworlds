import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('crossmatch_summarylow.csv')
df2 = pd.read_csv("new100psc_gaiasample.csv")

def f(x):
    return 7.8*x + 1.6

df['grp']= df['phot_g_mean_mag']-df['phot_rp_mean_mag']
df['distance']=1000/df['parallax']
df['mag'] = (df['phot_g_mean_mag']-(5*np.log10(df['distance']/10)))

#df = df[df['mag'] > f(df['grp'])]

df2['grp']= df2['phot_g_mean_mag']-df2['phot_rp_mean_mag']
df2['distance']=1000/df2['parallax']
df2['mag'] = (df2['phot_g_mean_mag']-(5*np.log10(df2['distance']/10)))

#df2 = df2[df2['mag'] > f(df2['grp'])]

#combined = pd.concat([df, df2], ignore_index=True)
#combined.to_csv("combined_highmetal8_28.csv", index=False)

plt.scatter(df2['grp'], df2['mag'], color = 'red', s = 0.4, label = '100 psc Sample')
plt.scatter(df['grp'], df['mag'], s=0.6,color='blue', label='Filtered Sample')
plt.xlabel('G-Rp')
plt.ylabel('Absolute Magnitude')
plt.title('Absolute Magnitude vs. G-Rp') 
x_vals = np.linspace(df['grp'].min(), df['grp'].max(), 200)
#plt.plot(x_vals, f(x_vals), color="red", label="Cutoff Function")
plt.xlim(0.5, 1.75)
plt.ylim(5,15)
plt.gca().invert_yaxis()
plt.show()