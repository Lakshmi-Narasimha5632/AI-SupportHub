from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    ordering = ("email",)

    list_display = (
        "email",
        "full_name",
        "role",
        "auth_provider",
        "is_active",
        "is_staff",
    )

    search_fields = ("email", "full_name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Information", {"fields": ("full_name",)}),
        ("Permissions", {
            "fields": (
                "role",
                "auth_provider",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "full_name",
                "password1",
                "password2",
                "role",
                "is_staff",
                "is_superuser",
            ),
        }),
    )