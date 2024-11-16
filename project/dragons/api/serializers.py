import datetime
from rest_framework import serializers
import pytz

from project.dragons.models import Dragon
from project.dragons.utils import calculate_level


class DragonSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    days_until_next_level = serializers.SerializerMethodField()

    class Meta:
        model = Dragon
        fields = ("id", "name", "food_percent", "happiness_percent", "dragon_type", "date_created", "user_id", "level", "days_until_next_level")

    def get_user_id(self, obj):
        return obj.user.id

    def get_level(self, obj):
        return calculate_level(obj)

    def get_days_until_next_level(self, obj):
        current_date = datetime.datetime.now(pytz.UTC)
        delta = current_date - obj.date_created

        # Calculate days since the last full week
        days_since_last_full_week = delta.days % 7

        # Days until the next full week
        return 7 - days_since_last_full_week if days_since_last_full_week != 0 else 0

    def create(self, validated_data):
        user = self.context['request'].user
        print('user', user)
        validated_data['user'] = user
        return super().create(validated_data)
