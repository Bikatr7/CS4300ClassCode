import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task3 import number_check, first_10_primes, sum_1_to_100

def test_number_check():
    assert number_check(5) == "positive"
    assert number_check(-3) == "negative"
    assert number_check(0) == "zero"
    assert number_check(100) == "positive"
    assert number_check(-0.0) == "zero"

def test_first_10_primes():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert first_10_primes() == expected
    assert len(first_10_primes()) == 10
    assert all(n > 1 for n in first_10_primes())

def test_sum_1_to_100():
    assert sum_1_to_100() == 5050
    assert isinstance(sum_1_to_100(), int)
    assert sum_1_to_100() == sum(range(1, 101))

if(__name__ == "__main__"):
    pytest.main([__file__, "-v"]) 