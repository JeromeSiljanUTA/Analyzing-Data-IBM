# Getting Started Analyzing Data in Python

|Pandas Type|Python Type|Description|
|-----------|-----------|-----------|
|`object`|`string`|numbers and strings|
|`int64` |`int`|numbers |
|`float64`|`float`|numbers with decimals|
|`datetime64, timedelta[ns]`|`datetime module`|time data|

 - `df.dtypes` returns data types of data
 - `df.describe()` shows data summary (skips rows and columns without numbers)
 - `df.describe(all)` shows data summary (including objects)
   - unique: number of distinct objects
   - top: most repeated
   - frequency: frequency of top
