from django.contrib            import admin
from django.contrib.auth.admin import UserAdmin
from .                         import models

@admin.register(models.User)      #데코레이터와 마찬가지로 동이할게 작동 = admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile",
            {
                "fields":
                    ("language",
                    "birthday",
                    "gender",
                    "currency",
                    "bio",
                    "avatar",
                    "superhost"
                    )
            },
        ),
    )
