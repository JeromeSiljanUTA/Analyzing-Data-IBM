# Model Evaluation and Refinement
Two types of data sets:
1. In sample (training)
 - Usually greater
2. Out of sample (test)
 - Used for seeing how prediction performs

The idea is that you use more samples to predict new values. These values are compared with the out of sample set to measure accuracy

```
from sklearn.model_selection import train_test_spli
train_test_split()
```

## Generalization Error
 - Shows actual values vs predicted values
 - Improved by more datao

## Cross Validation
 - Data set is split into k equal groups (folds)
 - Some folds are used as data sets, others as test sets
 - Create score for each combination of folds
 - Use average results as estimate for error

     ```
from sklearn.model_selection import cross_val_score
cross_val_score() # cv manages number of folds
```
