from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
def home(request):
    return JsonResponse({"message": "Welcome to the Book API!"})
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for full CRUD operations on Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer