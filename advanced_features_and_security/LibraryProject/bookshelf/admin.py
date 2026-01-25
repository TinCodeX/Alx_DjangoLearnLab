from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(Book)
# ✅ Custom User Admin class
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "is_staff", "date_of_birth")

# ✅ Register with admin.site.register to satisfy ALX
admin.site.register(CustomUser, CustomUserAdmin)
