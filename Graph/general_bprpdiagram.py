import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy.polynomial.chebyshev as cheb

df = pd.read_csv('crossmatch_summarylow.csv')
df2 = pd.read_csv("new100psc_gaiasample.csv")

df['distance']=1000/df['parallax']
df['mag'] = (df['phot_g_mean_mag']-(5*np.log10(df['distance']/10)))

#df = df[df['mag'] > f(df['grp'])]

df2['distance']=1000/df2['parallax']
df2['mag'] = (df2['phot_g_mean_mag']-(5*np.log10(df2['distance']/10)))

#df2 = df2[df2['mag'] > f(df2['grp'])]

#combined = pd.concat([df, df2], ignore_index=True)
#combined.to_csv("combined_highmetal8_28.csv", index=False)

#degree = 3
#coeffs = np.polyfit(df['grp'], df['mag'], degree)
#poly = np.poly1d(coeffs)
#x_vals = np.linspace(df['grp'].min(), df['grp'].max(), 500)
#cheb_fit = cheb.Chebyshev.fit(df2['bp_rp'], df2['mag'], degree)
#plt.plot(x_vals, cheb_fit(x_vals), color="green", linewidth=2, label=f"Chebyshev (deg {degree})")

plt.scatter(df['bp_rp'], df['mag'], s=0.6,color='blue', label='Filtered Sample')
plt.scatter(df2['bp_rp'], df2['mag'], color = 'red', s = 0.4, label = '100 psc Sample')
poly = np.polyfit(df2['bp_rp'], df2['mag'], deg=3)

fig, ax = plt.subplots()
plt.plot(df2['bp_rp'], label='data')
plt.plot(np.polyval(poly, df2['bp_rp']), label='fit')
#ax.legend()
plt.xlabel('Bp-Rp')
plt.ylabel('Absolute Magnitude')
plt.title('Absolute Magnitude vs. Bp-Rp') 
#x_vals = np.linspace(df['bp_rp'].min(), df['bp_rp'].max(), 200)
#plt.plot(x_vals, f(x_vals), color="red", label="Cutoff Function")
#plt.xlim(0.5, 5)
#plt.ylim(3,20)
plt.gca().invert_yaxis()
plt.show()