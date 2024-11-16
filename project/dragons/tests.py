from django.test import TestCase

from project.dragons.models import Dragon
from project.users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class DragonTestCase(TestCase):
    email = "test@example.com"

    def setUp(self) -> None:
        user = User.objects.create(
            email=self.email
        )
        user.set_password('Password99!')
        user.save()
        token = Token.objects.get_or_create(user=user)[0]

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        Dragon.objects.create(name="first", user=user, dragon_type=Dragon.BLUE)

    def test_get_endpoint(self):
        response = self.client.get("/api/dragons/")

        self.assertEqual(response.status_code, 200)

    def test_post_endpoint(self):
        data = {
            "name": "Boy",
            "dragon_type": "red"
        }

        response = self.client.post("/api/dragons/", data=data)

        self.assertEqual(response.status_code, 200)

    def test_patch_endpoint(self):
        data = {
            "name": "Boy",
            "food_percent": 50,
            "happiness_percent": 75
        }

        response = self.client.patch("/api/dragons/1/", data=data)

        self.assertEqual(response.status_code, 200)

    def test_destroy_endpoint(self):
        response = self.client.delete("/api/dragons/1/")

        self.assertEqual(response.status_code, 204)
