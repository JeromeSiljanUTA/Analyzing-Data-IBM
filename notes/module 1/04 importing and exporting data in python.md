# Importing and Exporting Data in Python

## Importing

 - Format (csv, json, xlsx, etc.)
 - File Path (where data is stored)

## Getting Data

 - Each row is one *data point*
 - Properties are associated with each data point


## Reading data in pandas
### Import into data frame

  ``` 
  import pandas as pd

  url = "/path/to/file"

  // df --> data frame

  df = pd.read_csv(url)   //assumes data header

  df = pd.read_csv(url, header = None)   //doesn't assume data header
  111
  ```

### Print data frame

  `print(df) `

### Assign column names
  ```
  headers = ["symboling", "normalized-losses", "etc"]

  df.columns = deaders
  ```

## Exporting Data
  ```
  path = "/path/to/file"
  df.to_csv(path)
  ```
