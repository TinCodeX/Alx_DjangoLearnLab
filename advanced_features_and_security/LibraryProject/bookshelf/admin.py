from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Author, Library

# ----------------------
# Register Book, Author, Library models
# ----------------------
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)

# ----------------------
# Custom User Admin
# ----------------------
class CustomUserAdmin(UserAdmin):
    # Add extra fields to the user admin
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Columns to display in the admin list view
    list_display = ("username", "email", "is_staff", "date_of_birth")

# Register CustomUser with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
