import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from task5 import get_first_three_books, student_database

def test_book_list_slicing():
    books = get_first_three_books()
    assert len(books) == 3
    assert all(isinstance(book, dict) for book in books)
    assert "The Hobbit" in [book["title"] for book in books]

def test_student_database():
    db = student_database()
    assert len(db) == 5
    assert "S001" in db.values()
    assert "Charlie Brown" in db.keys()
    assert isinstance(db, dict)

if(__name__ == "__main__"):
    pytest.main([__file__, "-v"]) 