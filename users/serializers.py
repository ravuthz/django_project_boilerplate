from django.contrib.auth.models import Permission, Group
from rest_framework.serializers import ModelSerializer

from .models import User


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name", "content_type", "codename")


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "permissions")


class UserSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "types",
            "phone",
            "email",
            "avatar",
            "password",
        )
        model = User
        extra_kwargs = {"password": {"write_only": True}}