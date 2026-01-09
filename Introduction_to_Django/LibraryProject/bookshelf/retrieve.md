# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve a specific book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# Output: ('1984', 'George Orwell', 1949)
```
