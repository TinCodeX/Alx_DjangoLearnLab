import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
print("Books by", author.name, ":", list(books_by_author))

# List all books in a library
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()
print("Books in", library.name, ":", list(books_in_library))

# Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of", library.name, ":", librarian.name)
