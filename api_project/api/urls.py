from django.urls import path
from .views import BookList
from .views import home

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', home, name='home'),
]
