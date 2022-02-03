# Linear Regression And Multiple Linear Regression

## Linear Regression
 - Uses one independent variable to make a prediction

## Multiple Linear Regression
 - Uses multiple independent variables to make a prediction

## Simple Linear Regression
$\LARGE{y = b_0 + b_1x}$
 - $y$: Estimated response
 - ${b_0}$: Intercept
 - ${b_1}$: Slope of regression line
 - Looking for $b_0, b_1$
 - x is independent, y is dependent

  ```
  import matplotlib.pyplot as plt
  from sklearn.linear_model import LinearRegression

  lm = LinearRegression()

  lm.fit(x, y)
        
  plt.plot(x, lm.predict(x))
  ```

## Multiple Linear Regression
 - $\LARGE{y = b_0 + b_1x_1 + b_2x_2 + b_3x_3...}$
 - Same thing, but you can use an array for the independent variable
