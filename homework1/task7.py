import numpy as np

## calculates the mean, median, and standard deviation of a list of numbers
def calculate_stats(numbers):
    arr = np.array(numbers)
    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std": np.std(arr)
    }

## calculates the determinant and inverse of a matrix
def matrix_operations():
    matrix = np.array([[1, 2], [3, 4]])
    return {
        "determinant": np.linalg.det(matrix),
        "inverse": np.linalg.inv(matrix)
    } 