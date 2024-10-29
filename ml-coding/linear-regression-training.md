# 🟡 Linear Regression (Training)

Now that you've implemented `get_model_prediction()` for a model, it's time to implement the training loop. At every iteration of the training loop, the previous function as well as `get_derivative()` should be called in order to perform gradient descent.

Your goal is to implement the `train_model()` function, which has the following as input:

1. `X`: The dataset for training the model. `X.length = n`and `X[i].length = 3 for 0 <= i < n`.
2. `Y`: The correct answers from the dataset. `Y.length = n`.
3. `num_iterations`: The number of iterations to run gradient descent for. `num_iterations > 0`.
4. `initial_weights`: The initial weights for the model (w1,w2,w3w1​,w2​,w3​). `initial_weights.length = 3`.

Return the final weights after training in the form of a NumPy array with dimension 3.

**Example 1:**

```java
Input:
X = [[1, 2, 3], [1, 1, 1]]
Y = [6, 3]
num_iterations = 10
initial_weights = [0.2, 0.1, 0.6]

Output:
[0.50678, 0.59057, 1.27435]
```

Note: The `get_derivative()` function is provided for you since it's rare for machine learning engineers or data scientists to calculate them by hand. In future problems, you will use a library like PyTorch to calculate the derivatives for you.

