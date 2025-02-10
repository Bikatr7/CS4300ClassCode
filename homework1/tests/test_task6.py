import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task6 import count_words

## basically this parameterizes the test so that it can be run with different files
@pytest.mark.parametrize("filename,expected", [
    ("task6_read_me.txt", 104)
])
def test_word_count(filename, expected):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(test_dir, '..', filename)
    assert count_words(file_path) == expected

if(__name__ == "__main__"):
    pytest.main([__file__, "-v"]) 