# Data Normalization In Python

 - Needs to be done so that data isn't skewed

## Normalization Methods
1. Simple feature scaling: $x_{new} = \frac{x_{old}}{x_{max}}$

   - Values range between 0 and 1
   - Values are measured as a fraction of the maximum
2. Min-Max: $x_{new} = \frac{x_{old}-x_{min}}{x_{max}-x_{min}}$

   - Values range between 0 and 1
3. Z-score: $x_{new} = \frac{x_{old} - \mu}{\sigma}$

   - $\mu$ is the average
   - $\sigma$ is the standard deviation
   - Values show distance from mean

## Useful Python Methods
 - `mean()`
 - `std() #standard deviation`
 - `max()`
 - `min()`
