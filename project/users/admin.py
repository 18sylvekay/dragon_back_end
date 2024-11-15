from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (
            "Login",
            {
                "fields": ("email", "password")
            }
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            }
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined")
            }
        ),
    ]
    ordering = ["email"]

    list_display = ["email"]
