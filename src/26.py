import numpy as np

def square_matrix(matrix):
    """
    This function takes a matrix and returns its square.
    
    Args:
    - matrix (list of lists): A 2D list representing the matrix to be squared.

    Returns:
    - list: The square version of the input matrix.
    """
    return np.array([np.square(row) for row in matrix])

# Example usage
matrix = [[1, 2], [3, 4]]
squared_matrix = square_matrix(matrix)
print(squared_matrix)
