# 🟢 Linear Regression (Forward)

Your task is to implement linear regression, a statistical model that ends up being the foundation of neural networks. You can learn more from the [Complete Explanation of Linear Regression](https://www.youtube.com/watch?v=K9xTjTP0vVw) or by reading the description below.

Your must implement `get_model_prediction()` which returns a prediction value for each dataset value, and `get_error()`which calculates the error for given prediction data.

**Inputs - `get_model_prediction`:**

* `X` - the dataset to be used by the model to predict the output. `len(X) = n`, and `len(X[i]) = 3 for 0 <= i < n`.
* `weights` - the current w1w1​, w2w2​, and w3w3​ weights for the model. `len(weights) = 3`.

**Inputs - `get_error`:**

* `model_prediction` - the model's prediction for each training example. `len(model_prediction) = n`.
* `ground_truth` - the correct answer for each example. `len(ground_truth) = n`.

```python
import numpy as np
from numpy.typing import NDArray

# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        return np.round(np.matmul(X, weights), 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        # assumption: Calculating Mean Square Error

        return np.round(np.mean(np.square(model_prediction - ground_truth)), 5)
```
