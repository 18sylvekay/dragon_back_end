from django.db import models


class Dragon(models.Model):
    name = models.CharField(max_length=50)
    food_percent = models.PositiveIntegerField(default=60)
    happiness_percent = models.PositiveIntegerField(default=60)

    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'users.User',
        related_name='dragons',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('id', 'date_created')

    def __str__(self):
        return f"Dragon: {self.name}"
