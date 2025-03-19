# Importing necessary libraries
import numpy as np
from scipy.optimize import minimize

# Defining the function to be optimized
def objective_function(x):
    # Define the mathematical expression that represents your project's function
    return x ** 2 + np.sin(x)

# Setting the initial values for the variables
x0 = [1, 2, 3]

# Optimizing the function using the "minimize" function from scipy.optimize
result = minimize(objective_function, x0)

# Printing the optimized values
print("Optimized values:", result.x)
