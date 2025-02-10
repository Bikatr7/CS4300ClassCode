import pytest
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task7 import calculate_stats, matrix_operations

## ensures the mean, median, and standard deviation are correct
def test_calculate_stats():
    stats = calculate_stats([1, 2, 3, 4, 5])
    assert pytest.approx(stats["mean"]) == 3.0
    assert pytest.approx(stats["median"]) == 3.0
    assert pytest.approx(stats["std"], rel=1e-3) == 1.4142

## ensures the determinant and inverse of a matrix are correct
def test_matrix_operations():
    results = matrix_operations()
    assert pytest.approx(results["determinant"]) == -2.0
    assert np.allclose(results["inverse"], np.array([[-2.0, 1.0], [1.5, -0.5]]))

if(__name__ == "__main__"):
    pytest.main([__file__, "-v"]) 