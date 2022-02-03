# Dealing with Missing Values in Python 

## Missing values appear as
 - ?
 - N/A
 - 0
 - Blank cell

## Solutions
 - Drop variable
 - Drop entry
 - Replacing data 
 - Leave it alone

### Replacing data
 - Replace with average value
 - Replace with mode (useful if not numbers)
 - Replace based on other functions 


## How to Drop Missing Values

`df.dropna()`
 - drop rows
 - drop columns
 - `axis = 0` drops rows
 - `axis = 1` columns
 - `inplace = True` writes date back into data frame

## Replace Missing Values
`df.replace(missing_value, new_values)`
