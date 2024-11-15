import datetime
from rest_framework import serializers

from project.dragons.models import Dragon


class DragonSerializer(serializers.Serializer):
    user_id = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    days_until_next_level = serializers.SerializerMethodField()

    class Meta:
        model = Dragon
        fields = "__all__"

    def get_user_id(self, obj):
        return obj.user.id

    def get_level(self, obj):
        current_date = datetime.now()
        delta = current_date - obj.date_created

        # Calculate full weeks since date created
        return delta.days // 7

    def get_days_until_next_level(self, obj):
        current_date = datetime.now()
        delta = current_date - obj.date_created

        # Calculate days since the last full week
        days_since_last_full_week = delta.days % 7

        # Days until the next full week
        return 7 - days_since_last_full_week if days_since_last_full_week != 0 else 0
