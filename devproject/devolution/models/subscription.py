from django.db import models
from django.utils import timezone
from .user import User
from .devotional import Devotional


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    devotional = models.ForeignKey(Devotional, on_delete=models.CASCADE)
    sequence = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'devolution'

    def update_sequence(self, seq):
        self.sequence = seq;
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s:%s" % (self.user, self.devotional)

