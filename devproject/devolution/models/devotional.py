from django.db import models
from django.utils import timezone


class Devotional(models.Model):
    # The title of the devotional
    title = models.TextField()
    # A description of the devotional
    description = models.TextField(blank=True, default='')
    # The image displayed for this daily entry
    picture_url = models.TextField(blank=True, default='')
    # The URL short cut for this daily entry
    shortcut = models.TextField(blank=True, default='')

    # The date this entry was created
    created_date = models.DateTimeField(default=timezone.now)
    # The date this entry was published
    published_date = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'devolution'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def is_published(self):
        return (self.published_date is not None
                and self.published_date <= timezone.now())

    def short_name(self):
        if self.shortcut != '':
            return self.shortcut
        else:
            return self.pk

    def __str__(self):
        return self.title


def lookup_devotional(devo_id):
    if len(devo_id) > 0:
        try:
            id = int(devo_id)
        except ValueError:
            # Is not an int - Look up string value
            try:
                entry = Devotional.objects.get(shortcut=devo_id)
            except Devotional.DoesNotExist:
                return None
        else:
            # Is an int - Look up integer value
            try:
                entry = Devotional.objects.get(pk=id)
            except Devotional.DoesNotExist:
                return None

        return entry
    else:
        return None



