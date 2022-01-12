# Data Formatting in Python

> Makes sure data is easily understandable


## Applying calculations to an entire column

`df["city-mpg"] = 235/df["city-mpg"]`   divides all the values of city-mpg by 235

`df.rename(columns=("city-mpg": "city-L/100km"), inplace=True)`   renames column "in place"

## Changing data types

### Identify
`df.dtypes()`

### Convert
`df.astype("int")`

