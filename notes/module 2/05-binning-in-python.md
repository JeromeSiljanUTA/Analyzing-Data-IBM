# Binning in Python

 - Group values into "bins"

## Example
Price category from 5000 to 45000

|Bins|Values|
|----|------|
|Low|5000-12000|
|Mid|12000-35000|
|High|35000-45500|

## Python Methods
 - `np.linspace(min, max, number_of_bins)`
   - returns array of bins
 - `pd.cut(target_column, bins, labels`
   - paired with linspace to create labels for bins
