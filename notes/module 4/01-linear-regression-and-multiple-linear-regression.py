import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

df = pd.read_csv("data.csv")

x = df.hours
y = df.score

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

lm.fit(x, y)
      
plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.scatter(x, y)
plt.plot(x, lm.predict(x))
plt.show()
