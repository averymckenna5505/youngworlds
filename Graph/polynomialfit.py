import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.chebyshev as cheb

# Set up data frames and variables
psc_sample = pd.read_csv("new100psc_gaiasample.csv")
catalog_sample = pd.read_csv("combined_filtered8_26.csv")

psc_sample['distance']=1000/psc_sample['parallax']
psc_sample['mag'] = (psc_sample['phot_g_mean_mag']-(5*np.log10(psc_sample['distance']/10)))
psc_sample['g-rp'] = (psc_sample['phot_g_mean_mag']-psc_sample['phot_rp_mean_mag'])

catalog_sample['distance']=1000/catalog_sample['parallax']
catalog_sample['mag'] = (catalog_sample['phot_g_mean_mag']-(5*np.log10(catalog_sample['distance']/10)))
catalog_sample['g-rp'] = (catalog_sample['phot_g_mean_mag']-catalog_sample['phot_rp_mean_mag'])

# Cut out white dwarfs
def f(x):
    return 1.5*x**2 + 10

psc_sample = psc_sample[psc_sample['mag'] < f(psc_sample["bp_rp"])]
catalog_sample = catalog_sample[catalog_sample['mag'] < f(catalog_sample['bp_rp'])]

bp_rp_psc = psc_sample["bp_rp"].values
mag_psc = psc_sample["mag"].values
g_rp_psc = psc_sample['g-rp'].values

mask_psc = np.isfinite(psc_sample['bp_rp']) & np.isfinite(psc_sample['mag'])
bp_rp_psc = psc_sample.loc[mask_psc, 'bp_rp'].values
mag_psc = psc_sample.loc[mask_psc, 'mag'].values
g_rp_psc = psc_sample.loc[mask_psc,'g-rp'].values

bp_rp_cat = catalog_sample["bp_rp"].values
mag_cat = catalog_sample["mag"].values
g_rp_cat = catalog_sample['g-rp'].values

mask_cat = np.isfinite(catalog_sample['bp_rp']) & np.isfinite(catalog_sample['mag'])
bp_rp_cat = catalog_sample.loc[mask_cat, 'bp_rp'].values
mag_cat = catalog_sample.loc[mask_cat, 'mag'].values
g_rp_cat = catalog_sample.loc[mask_cat, 'g-rp'].values

# Plot mag vs. bp_rp

#plt.scatter(bp_rp_psc, mag_psc, color="blue", s = 0.1, label="Gaia")
#plt.scatter(bp_rp_cat, mag_cat, color="red", s = 0.1, label="Catalog")
plt.scatter(g_rp_psc, mag_psc, color = "blue", s = 0.1, label = "Gaia")
plt.scatter(g_rp_cat, mag_cat, color = "red", s = 0.1, label = "Catalog")
plt.ylim(min(mag_psc), max(mag_psc)) 

# Chebyshev polynomial setup
degree = 7
cheb_fit = cheb.Chebyshev.fit(bp_rp_psc, mag_psc, degree)

x_fit = np.linspace(min(bp_rp_psc), max(bp_rp_psc), 500)
y_fit = cheb_fit(x_fit) + 0.7

shifted_fit_psc_values = cheb_fit(psc_sample['bp_rp'].values) + 0.7
shifted_fit_cat_values = cheb_fit(catalog_sample['bp_rp'].values) + 0.7

#plt.plot(x_fit, y_fit, color="red", linewidth = 2, label=f"{degree}-degree fit")
plt.gca().invert_yaxis()

print("Chebyshev coefficients:", cheb_fit.coef)

# Filtering datasets by polynomial cutoff and saving csv files
psc_low = psc_sample[psc_sample['mag'] > shifted_fit_psc_values]
cat_low = catalog_sample[catalog_sample['mag'] > shifted_fit_cat_values]
psc_high = psc_sample[psc_sample['mag'] < shifted_fit_psc_values]
cat_high = catalog_sample[catalog_sample['mag'] < shifted_fit_cat_values]

combined1 = pd.concat([psc_low, cat_low], ignore_index=True)
combined1.to_csv("catalog_and_100psc_low.csv", index=False)

combined2 = pd.concat([psc_high, cat_high], ignore_index=True)
combined2.to_csv("catalog_and_100psc_high.csv", index=False)

plt.show()