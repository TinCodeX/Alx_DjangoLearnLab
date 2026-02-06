# Advanced API Development with Django REST Framework

## Project Overview
This project demonstrates advanced API development using Django REST Framework. 
It includes custom serializers, nested relationships, generic views, permissions, 
and optional filtering.

## API Views Overview

### Book Endpoints
- **GET /api/books/**: List all books (public). Supports filtering by `year`.
- **GET /api/books/<id>/**: Retrieve single book (public).
- **POST /api/books/create/**: Create new book (authenticated only).
- **PUT /api/books/<id>/update/**: Update book (authenticated only).
- **DELETE /api/books/<id>/delete/**: Delete book (authenticated only).

Permissions are enforced via DRF permission classes. Validation is handled
through custom serializers.

## Setup Instructions
1. Clone this repo.
2. Install dependencies: `pip install django djangorestframework`.
3. Run migrations: `python manage.py migrate`.
4. Create a superuser: `python manage.py createsuperuser`.
5. Start server: `python manage.py runserver`.
6. Access API at `http://127.0.0.1:8000/api/books/`.
## Testing

Unit tests were written using Django REST Framework’s APITestCase.
The tests cover CRUD operations, permissions, and filtering/searching/ordering.

To run the tests:

```bash
python manage.py test api
