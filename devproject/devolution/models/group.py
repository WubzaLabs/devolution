from django.db import models
from django.utils import timezone
from .devotional import Devotional


class Group(models.Model):
    title = models.TextField()
    devotional = models.ForeignKey(Devotional, on_delete=models.CASCADE)

    order = models.IntegerField(default=0)

    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'devolution'

    def __str__(self):
        return "%s:%s" % (self.devotional, self.title)

