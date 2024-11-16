import datetime
from django.db import models


class Dragon(models.Model):
    GREEN = "green"
    BLUE = "blue"
    RED = "red"

    TYPE_CHOICES = (
        (GREEN, "Green"),
        (BLUE, "Blue"),
        (RED, "Red"),
    )

    name = models.CharField(max_length=50)
    food_percent = models.PositiveIntegerField(default=60)
    happiness_percent = models.PositiveIntegerField(default=60)
    dragon_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    date_created = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(
        'users.User',
        related_name='dragons',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('id', 'date_created')

    def __str__(self):
        return f"Dragon: {self.name}"
