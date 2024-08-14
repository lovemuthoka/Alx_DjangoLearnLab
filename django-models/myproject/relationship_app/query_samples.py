
from django.db.models import Q
from .models import Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def get_books_in_library(library_name):
    return Book.objects.filter(library__name=library_name)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)

if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    books_by_author =  get_books_by_author(author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    books_in_library =get_books_in_library (library_name)
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    librarian =  get_librarian_for_library(library_name)
    print(f"Librarian for {library_name}: {librarian.name if librarian else 'No librarian assigned.'}")