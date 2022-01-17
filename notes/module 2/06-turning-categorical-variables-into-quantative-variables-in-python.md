# Turning Categorical Variables Into Quantative Variables in Python

 - Need numbers, not strings

## Example (expected result)
|Car|Fuel_type|gas|diesel|
|---|---------|---|------|
|A|gas|1|0|
|B|diesel|0|1|
|C|gas|1|0|
|D|gas|1|0|

## Python Methods
`pd.get_dummies(feature)`
