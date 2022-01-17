import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("data.csv")

x = data.iloc[:,1].to_numpy().reshape(-1, 1)
y = data.iloc[:,2].to_numpy()

lReg = LinearRegression()
lReg.fit(x, y)

pReg = PolynomialFeatures(degree = 2)
xPoly = pReg.fit_transform(x)
pReg.fit(xPoly, y)
lReg2 = LinearRegression()
lReg2.fit(xPoly, y)

plt.scatter(x, y)
plt.plot(x, lReg.predict(x))
plt.plot(x, lReg2.predict(x))
plt.show()
