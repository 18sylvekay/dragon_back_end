from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Overriden properties
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "A user with that email address already exists.",
        }
    )

    # Normal Properties
    food_owned = models.PositiveIntegerField(default=0)
    treasure_owned = models.PositiveIntegerField(default=0)

    # Methods
    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ("email",)
