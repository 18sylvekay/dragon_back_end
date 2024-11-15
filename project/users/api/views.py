from django.contrib.auth import authenticate
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
        if self.action == "sign_up":
            return []
        else:
            return [permissions.IsAuthenticated()]

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
