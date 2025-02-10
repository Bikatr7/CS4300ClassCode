import numpy as np

def calculate_stats(numbers):
    arr = np.array(numbers)
    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std": np.std(arr)
    }

def matrix_operations():
    matrix = np.array([[1, 2], [3, 4]])
    return {
        "determinant": np.linalg.det(matrix),
        "inverse": np.linalg.inv(matrix)
    } 