"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bookshelf import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Book CRUD views
    path("books/", views.book_list, name="book_list"),
    path("books/create/", views.book_create, name="book_create"),
    path("books/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),

    # ExampleForm view
    path("example_form/", views.example_form_view, name="example_form"),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
