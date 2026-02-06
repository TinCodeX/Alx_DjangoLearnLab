from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions,
    filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up test data and authenticated user.
        """
        self.client = APIClient()

        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        # Create sample books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William Vincent",
            publication_year=2018
        )

        self.book2 = Book.objects.create(
            title="Two Scoops of Django",
            author="Daniel Roy Greenfeld",
            publication_year=2020
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"

    # -------------------------------
    # READ TESTS (PUBLIC ACCESS)
    # -------------------------------

    def test_list_books(self):
        """
        Anyone should be able to list books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Anyone should be able to retrieve a single book.
        """
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -------------------------------
    # CREATE TESTS (AUTH REQUIRED)
    # -------------------------------

    def test_create_book_unauthenticated(self):
        """
        Unauthenticated users should NOT create books.
        """
        data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "publication_year": 2008
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """
        Authenticated users should create books.
        """
        self.client.login(username="testuser", password="testpassword123")

        data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "publication_year": 2008
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -------------------------------
    # UPDATE TESTS
    # -------------------------------

    def test_update_book_authenticated(self):
        """
        Authenticated users should update books.
        """
        self.client.login(username="testuser", password="testpassword123")

        update_url = f"/api/books/update/{self.book1.id}/"
        data = {
            "title": "Django for Professionals",
            "author": self.book1.author,
            "publication_year": self.book1.publication_year
        }

        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Django for Professionals")

    def test_update_book_unauthenticated(self):
        """
        Unauthenticated users should NOT update books.
        """
        update_url = f"/api/books/update/{self.book1.id}/"
        data = {"title": "Hacked Title"}

        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------
    # DELETE TESTS
    # -------------------------------

    def test_delete_book_authenticated(self):
        """
        Authenticated users should delete books.
        """
        self.client.login(username="testuser", password="testpassword123")

        delete_url = f"/api/books/delete/{self.book1.id}/"
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """
        Unauthenticated users should NOT delete books.
        """
        delete_url = f"/api/books/delete/{self.book1.id}/"
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------
    # FILTER / SEARCH / ORDER TESTS
    # -------------------------------

    def test_filter_books_by_author(self):
        """
        Test filtering books by author.
        """
        response = self.client.get(self.list_url, {"author": "William Vincent"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url, {"search": "Django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["publication_year"],
            self.book2.publication_year
        )
