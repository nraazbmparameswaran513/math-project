import numpy as np
import pandas as pd

def calculate_mean(data):
    """
    Calculate the mean of a given dataset.
    
    Parameters:
        data (list or np.ndarray): The dataset containing numerical values.
        
    Returns:
        float: The mean value of the provided dataset.
    """
    if not isinstance(data, list) and not isinstance(data, pd.DataFrame):
        raise ValueError("The input must be a list or a pandas DataFrame.")
    
    if len(data) == 0:
        return None
    
    if isinstance(data[0], (int, float)):
        mean = np.mean(data)
    elif isinstance(data[0], pd.Series):
        mean = data.mean()
    else:
        raise ValueError("Unsupported data type. Use a list or DataFrame.")
    
    return mean

# Example usage
data_points = [1, 2, 3, 4, 5]
mean_value = calculate_mean(data_points)
print(f"The mean of the dataset is: {mean_value}")
