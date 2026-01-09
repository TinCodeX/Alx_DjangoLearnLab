# Update Operation

```python
from bookshelf.models import Book

# Get the book
b = Book.objects.get(title="1984")

# Update the title
b.title = "Nineteen Eighty-Four"
b.save()

# Confirm the update
Book.objects.get(id=b.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
```
