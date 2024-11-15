from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Overriden properties
    username = None
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "A user with that email address already exists.",
        }
    )

    # Methods
    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ("email",)
