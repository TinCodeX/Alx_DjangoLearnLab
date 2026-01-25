from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# List books with safe search (avoid SQL injection)
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(title__icontains=query)  # ORM safe
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Create book
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

# Edit book
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form})

# Delete book
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
# settings.py
# DEBUG=False to avoid sensitive info leaks
# SECURE_BROWSER_XSS_FILTER=True: enables XSS filter in browsers
# X_FRAME_OPTIONS='DENY': prevents clickjacking
# CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE: cookies only sent over HTTPS
# CSP: restricts domains for scripts, styles, fonts, and images

# views.py
# Using Django ORM and ModelForms to prevent SQL injection
# @permission_required ensures only users with permissions can access views
