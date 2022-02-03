# Model Evaluation Using Visualization

## Simple Regression Plot
  ```
  import seaborn as sns
  sns.regplot(x = "independent", y = "dependent", data = df)
  plt.ylim(0, y)
  ```

## Residual Plot (for Linear Regression)
 - Measures error between expected and actual value
 - Expect 0 mean
 - No curvature 
 - Curvature suggests non linear function

     ```
     sns.residplot(df["independent"], df["dependent"])
     ```

## Distribution Plot
 - Compared predicted and actual value
 - Really good at showing diffeences
 ```
 ax1 = sns.distplot(df["independent"], hist = False)

 sns.distplot(Yhat, hist = False, ax = ax1)
 ```
