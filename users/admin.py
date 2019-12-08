from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# 이 데코레이터는 models.User를 CustomUserAdmin에서 쓸 수 있게 함
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):  # UserAdmin을 CustomUserAdmin에서 쓸 수 있게 함
    """ Custom User Admin """

    # list_display = ("username", "email", "gender",
    #                 "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )


# admin.site.register(models.User, CustomUserAdmin)
