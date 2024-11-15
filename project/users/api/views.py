from django.contrib.auth import (logout, login, authenticate)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from project.users.api.serializers import CreateUserSerializer, MeSerializer
from project.users.models import User
from rest_framework.response import Response


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_value_regex = "(?!(login|logout|password_change|password_reset|password_reset_submission|check_password_reset_link))[^/.]+"
    serializer_class = MeSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        if self.action == "sign_up" or self.action == "login":
            return []
        else:
            return [permissions.IsAuthenticated()]

    @action(detail=False, methods=["GET"])
    def me(self, request):
        me = self.get_queryset().first()
        serializer = self.get_serializer(me)

        return Response(serializer.data)

    @method_decorator(never_cache)
    @action(detail=False, methods=["POST"])
    def sign_up(self, request):
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            user = authenticate(
                username=request.data["email"],
                password=request.data["password"],
            )

            token = Token.objects.get_or_create(user=user)[0]
            return Response(
                {
                    "drf_token": token.key,
                    "user_data": MeSerializer(user).data,
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(never_cache)
    @action(detail=False, methods=["POST"])
    def login(self, request):
        data = request.data
        errors = {}

        user = authenticate(
            username=data["email"],
            password=data["password"],
        )

        if user is None:
            errors["non_field_errors"] = "Your username or password were incorrect."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "drf_token": token.key,
            "user_data": MeSerializer(user).data,
        })

    @method_decorator(never_cache)
    @action(detail=False, methods=["POST"])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
