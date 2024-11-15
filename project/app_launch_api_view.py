from rest_framework.response import Response
from rest_framework.views import APIView

from project.users.api.serializers import MeSerializer


class AppLaunchAPIView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        response_dict = {}

        if request.user.is_authenticated:
            response_dict["user_data"] = MeSerializer(request.user).data

        return Response(response_dict)
