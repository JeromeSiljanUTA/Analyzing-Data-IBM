import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("data.csv")

#x = data.Level.to_numpy().reshape(-1, 1)
#y = data.Salary.to_numpy()

x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y = [-64, -27, -8, -1, 0, 1, 8, 27, 64]

print(np.polyfit(x, y, 2))

yhat1 = (-5.34 * 10**(-16)) + (1.18 * 10**(1)) + (9.47 * 10**(-15))

print(yhat1)

#plt.plot(x, y)
#plt.show()
