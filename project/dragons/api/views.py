from rest_framework import viewsets, status

from project.dragons.api.serializers import DragonSerializer
from project.dragons.models import Dragon
from rest_framework.response import Response


class DragonViewSet(viewsets.ModelViewSet):
    serializer_class = DragonSerializer

    def get_queryset(self):
        return Dragon.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Return a 200 OK response with the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
