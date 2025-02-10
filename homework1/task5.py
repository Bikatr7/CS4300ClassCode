## hardcoded random books
def get_first_three_books():
    books = [
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "Dune", "author": "Frank Herbert"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
        {"title": "Foundation", "author": "Isaac Asimov"}
    ]
    return books[:3]

## hardcoded random student database
def student_database():
    return {
        "Alice Smith": "S001",
        "Bob Johnson": "S002",
        "Charlie Brown": "S003",
        "Diana Prince": "S004",
        "Bruce Wayne": "S005"
    } 