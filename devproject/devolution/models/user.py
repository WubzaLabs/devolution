from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.TextField()
    mobile = models.TextField()
    email = models.EmailField()
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'devolution'

    def __str__(self):
        return self.name

