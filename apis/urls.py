from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include("rest_framework.urls")),
]
