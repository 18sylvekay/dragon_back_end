from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from project.users.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'food_owned', 'treasure_owned')


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    password2 = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password2",
        ]

    def save(self):
        password = self.validated_data.pop("password")
        self.validated_data.pop("password2")

        user = User(**self.validated_data)
        user.set_password(password)
        user.save()

        token = Token.objects.get_or_create(user=user)[0]
        token.save()

    def validate(self, data):
        errors = {}

        # Check that new passwords match
        if data["password"] != data["password2"]:
            errors["password2"] = "The two password fields didn't match."

        # Check that password matches password requirements
        if "password2" not in errors:
            try:
                validate_password(password=data["password"])
            except ValidationError as e:
                errors["password2"] = e.messages[0]

        if errors:
            raise serializers.ValidationError(errors)

        return data
