# Ridge Regression
Prevents overfitting

Alpha parameter
 - Adjusts values of coefficients to help fit better
 - As alpha increases, coefficients decrease

```
from sklearn.linear_model import Ridge
RidgeModel = Ridge(alpha = 0.1)
RidgeModel.fit(X,y)

Yhat = RidgeModel.predict(X)
```

## Choosing Alpha value
 - Train model, find $R^2$
 - Choose with lowest $R^2$
