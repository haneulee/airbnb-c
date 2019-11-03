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
                )
            },
        ),
    )


# admin.site.register(models.User, CustomUserAdmin)
