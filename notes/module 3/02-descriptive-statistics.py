import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.argv[1])

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

df.replace("?", np.NaN, inplace = True)
df.dropna(inplace = True)
df.price = df.price.astype(int)

"""
df_test =df[["drive-wheels", "body-style", "price"]]
df_grp = df_test.groupby(["drive-wheels", "body-style"], as_index = False).mean()

df_piv = df_grp.pivot(index = "drive-wheels", columns = "body-style")

plt.pcolor(df_piv, cmap = "RdBu")
plt.colorbar()
plt.show()
"""
sns.regplot(x = "engine-size", y = "price", data = df)
plt.ylim(0,)
plt.show()
