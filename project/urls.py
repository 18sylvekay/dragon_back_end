"""
URL configuration for project.
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from project.users.api import views as UserViews
from project.dragons.api import views as DragonViews
from project.app_launch_api_view import AppLaunchAPIView

router = DefaultRouter()

router.register("users", UserViews.UserViewSet, basename="users")
router.register("dragons", DragonViews.DragonViewSet, basename="dragons")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/app-launch/", AppLaunchAPIView.as_view()),
    path('admin/', admin.site.urls),
]
