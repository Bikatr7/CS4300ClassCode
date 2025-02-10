import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task4 import calculate_discount

def test_with_integers():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(50, 10) == 45
    assert calculate_discount(200, 25) == 150

def test_with_floats():
    assert calculate_discount(100.0, 20.0) == pytest.approx(80.0)
    assert calculate_discount(49.99, 15.5) == pytest.approx(42.24, rel=1e-2)
    assert calculate_discount(199.95, 10.0) == pytest.approx(179.955)

def test_mixed_types():
    assert calculate_discount(100, 12.5) == pytest.approx(87.5)
    assert calculate_discount(75.99, 20) == pytest.approx(60.792)
    assert calculate_discount(150.0, 33) == pytest.approx(100.5)

def test_edge_cases():
    assert calculate_discount(0, 50) == 0
    assert calculate_discount(100, 0) == 100
    assert calculate_discount(100, 100) == 0

def test_non_numeric_input():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)
    with pytest.raises(TypeError):
        calculate_discount(100, "10")
    with pytest.raises(TypeError):
        calculate_discount([100], 10)

if(__name__ == "__main__"):
    pytest.main([__file__, "-v"]) 