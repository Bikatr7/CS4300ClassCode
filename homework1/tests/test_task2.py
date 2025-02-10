import sys
import os

## Add homework directory to Python path
test_dir = os.path.dirname(os.path.abspath(__file__))
homework_dir = os.path.dirname(test_dir)
sys.path.append(homework_dir)

from task2 import example_int, example_float, example_string, example_bool

## each func ensures the type is correct and the value is correct

def test_integer_type():
    assert isinstance(example_int, int), "Should be integer type"
    assert example_int == 42

def test_float_type():
    assert isinstance(example_float, float), "Should be float type"
    assert abs(example_float - 3.14159) < 1e-9

def test_string_type():
    assert isinstance(example_string, str), "Should be string type"
    assert example_string == "Python Type Check"

def test_boolean_type():
    assert isinstance(example_bool, bool), "Should be boolean type"
    assert example_bool is True


def run_tests():
    test_integer_type()
    test_float_type()
    test_string_type()
    test_boolean_type()
    print("Task 2 OK")

if(__name__ == "__main__"):
    run_tests()
