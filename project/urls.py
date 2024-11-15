"""
URL configuration for project.
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from project.users.api import views as UserViews
from project.app_launch_api_view import AppLaunchAPIView
from virgodev_user_basics.api.urls import router as virgodev_user_basics_router

router = DefaultRouter()

router.register("users", UserViews.UserViewSet, basename="users")

router.registry.extend(virgodev_user_basics_router.registry)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/app-launch/", AppLaunchAPIView.as_view()),
    path('admin/', admin.site.urls),
]
