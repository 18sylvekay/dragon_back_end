from django.test import TestCase

from project.users.models import User


class UserTestCase(TestCase):
    username = "user_1"
    email = "test@example.com"

    def setUp(self) -> None:
        User.objects.create(
            email=self.email
        )

    def test_sign_up_endpoint(self):
        data = {
            "email": "test2@example.com",
            "password": "thisismypassword99",
            "password2": "thisismypassword99",
        }
        response = self.client.post("/api/users/sign_up/", data=data)

        self.assertEqual(response.status_code, 200)
