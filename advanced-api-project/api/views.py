from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST VIEW WITH FILTERING, SEARCH, ORDERING
# -------------------------------

class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Features:
    - Filtering by title, author, publication_year
    - Searching by title and author
    - Ordering by title and publication_year

    Access:
    - Read-only for unauthenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# -------------------------------
# RETRIEVE VIEW
# -------------------------------

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/
    Retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------------
# CREATE, UPDATE, DELETE VIEWS
# -------------------------------

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/<pk>/
    Update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/<pk>/
    Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
