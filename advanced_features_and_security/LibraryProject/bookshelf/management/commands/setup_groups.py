from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create groups and assign permissions to Book"

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Viewers": ["can_view"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for perm_code in perms:
                try:
                    permission = Permission.objects.get(
                        codename=perm_code,
                        content_type__app_label="bookshelf"
                    )
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {perm_code} not found"))
            group.save()
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' updated with permissions"))
