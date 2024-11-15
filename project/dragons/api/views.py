from rest_framework import viewsets

from project.dragons.api.serializers import DragonSerializer
from project.dragons.models import Dragon


class DragonViewSet(viewsets.ModelViewSet):
    serializer_class = DragonSerializer

    def get_queryset(self):
        return Dragon.objects.filter(user=self.request.user)
