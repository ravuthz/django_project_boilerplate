import os

from django.contrib.auth.models import Group as BaseGroup, AbstractUser
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _


def get_upload_path(instance, filename):
    return os.path.join("users/{}/avatars/".format(instance.id), filename)


class Group(BaseGroup):
    pass


class User(AbstractUser):
    USER = 1
    ADMIN = 2
    SUPER = 3

    USER_TYPE_CHOICES = (
        (USER, "user"),
        (ADMIN, "admin"),
        (SUPER, "supervisor"),
    )

    password = models.CharField(
        _("password"), max_length=128, blank=True, null=True)
    phone = models.CharField(
        _("phone number"), max_length=14, blank=True, null=True)
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
    types = models.PositiveSmallIntegerField(
        blank=True, null=True, default=USER, choices=USER_TYPE_CHOICES,
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        swappable = "AUTH_USER_MODEL"

    readonly_fields = (
        "last_login",
        "date_joined",
    )

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def get_upload_path(self, filename):
        return get_upload_path(self, filename)
