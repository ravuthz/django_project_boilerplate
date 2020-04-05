# Create your views here.
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
