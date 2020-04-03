from django.contrib import admin, auth
from django.utils.translation import gettext_lazy as _

from .models import Group, User

# Register your models here.


personal_info = (
    _("Personal info"),
    {
        "fields": (
            "username",
            "first_name",
            "last_name",
            "phone",
            "email",
            "avatar",
        )
    },
)

permissions = (
    _("Permissions"),
    {
        "fields": (
            "is_active",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ),
    },
)


class GroupAdmin(auth.admin.GroupAdmin):
    pass


class UserAdmin(auth.admin.UserAdmin):
    list_display = (
        "id",
        "avatar",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_superuser",
        "is_staff",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email"
    )
    ordering = ("username",)

    fieldsets = (
        personal_info,
        permissions,
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined"
                )
            }
        ),
    )

    add_fieldsets = (
        personal_info,
        (
            _("Password"),
            {
                "fields": (
                    "password1",
                    "password2",
                )
            },
        ),
        permissions,
    )


admin.site.unregister(auth.models.Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
