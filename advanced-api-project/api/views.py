from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST AND RETRIEVE VIEWS
# -------------------------------

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Open to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/
    Retrieve a single book by ID. Open to everyone.
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
    Create a new book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Override create to add a custom response message.
        """
        response = super().create(request, *args, **kwargs)
        response.data = {
            "message": "Book created successfully!",
            "book": response.data
        }
        return response

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<pk>/update/
    Update an existing book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """
        Override update to add a custom response message.
        """
        response = super().update(request, *args, **kwargs)
        response.data = {
            "message": "Book updated successfully!",
            "book": response.data
        }
        return response

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/
    Delete a book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# -------------------------------
# OPTIONAL: Combined Retrieve + Update + Delete
# -------------------------------
# This is an alternative single view instead of separate update/delete
# Uncomment below if you want fewer classes.
#
# class BookDetailEditView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     GET / PUT / PATCH / DELETE /api/books/<pk>/
#     Combined retrieve, update, delete view.
#     Read-only for unauthenticated, write requires authentication.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
