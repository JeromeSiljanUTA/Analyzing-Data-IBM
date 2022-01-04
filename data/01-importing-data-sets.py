import pandas as pd 
import numpy as np

data_path = "imports-85.data"

df = pd.read_csv(data_path, header=None)    # import data and store in df, don't make first row header

print("printing first 10 rows")
df.head(10)

print("printing last 10 rows")
df.tail(10)

#########################
#    Adding Headers     #
#########################

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

print("headers\n", headers)

df.columns = headers

print("printing first 10 rows (after I set the headers)")
df.head(10)


#########################
#    Fixing bad data    #
#########################

df1 = df.replace("?", np.NaN)   # set all ? to NaN

df1.head(10)

df.head(20)

df = df1.dropna(subset=["price"])   # dropping all rows with price as NaN

df.head(20)

df.columns       # returns columns

#########################
#    Saving Dataset     #
#########################

df.to_csv("cleaned.csv", index=False)

#########################
#    Data Types         #
#########################

df.dtypes        # print types of columns of data

#########################
#  Statistical Summary  #
#########################

df.describe(include = "all")     # include all includes object types in summary as well

print(df[["length", "compression-ratio"]].describe())     # only summarizes columns selected 

print(df.info())
