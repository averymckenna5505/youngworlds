import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("gaia_data_full_new2(in) (1).csv")
#df2 = pd.read_csv("1753913181642O-result(in).csv")

df['distance']=1000/df['parallax']
df['magnitude'] = (df['phot_g_mean_mag']-(5*np.log10(df['distance']/10)))


#df2['magnitude'] = (df2['phot_g_mean_mag']-(2.5*np.log(10000/(df2['parallax']**2))))

#df['g-rp'] = (df['phot_g_mean_mag']-df['phot_rp_mean_mag'])

plt.scatter(df['phot_rp_mean_mag'], df['magnitude'], s=1,color='blue', label='Sample A')
#plt.scatter(df2['bp_rp'], df2['magnitude'], color='orange', label='Sample B')
plt.xlabel('Rp') 
plt.ylabel('Absolute Magnitude') 
plt.title('Absolute Magnitude vs. rp') 
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()