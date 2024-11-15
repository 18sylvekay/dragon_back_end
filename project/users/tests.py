from django.test import TestCase

from project.users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class UserTestCase(TestCase):
    email = "test@example.com"

    def setUp(self) -> None:
        user = User.objects.create(
            email=self.email
        )
        user.set_password('Password99!')
        Token.objects.get_or_create(user=user)[0]
        user.save()

    def test_me_endpoint(self):
        user = User.objects.get(email=self.email)
        token = Token.objects.get(user=user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get("/api/users/me/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["email"], self.email)

    def test_sign_up_endpoint(self):
        data = {
            "email": "test2@example.com",
            "password": "thisismypassword99",
            "password2": "thisismypassword99",
        }
        response = self.client.post("/api/users/sign_up/", data=data)

        self.assertEqual(response.status_code, 200)
