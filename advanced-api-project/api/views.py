from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST AND RETRIEVE VIEWS
# -------------------------------

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/
    Retrieve a single book. Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# CREATE, UPDATE, DELETE VIEWS
# -------------------------------

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/<pk>/
    Update a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/<pk>/
    Delete a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
