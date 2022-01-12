# pulling data
import pandas as pd

data_path = "../imports-85.data"

df = pd.read_csv(data_path, header=None)    # import data and store in df, don't make first row header

#########################
#    Adding Headers     #
#########################

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

fuel_df = pd.get_dummies(df["fuel-type"])
print("Number of diesel vehicles: " + str(fuel_df["diesel"].sum()))
print("Number of gas vehicles: " + str(fuel_df["gas"].sum()))
