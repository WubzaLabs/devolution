from django.db import models
from django.utils import timezone
from .devotional import Devotional
from .group import Group


class Entry(models.Model):
    # The devotional that this Entry is assigned to
    devotional = models.ForeignKey(Devotional, on_delete=models.CASCADE)
    # The grouping of entries within the devotional
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    # The overall position of this entry
    sequence_num = models.IntegerField()
    # The prefix to the title displayed on the entry page (e.g. Day 1, Week 1, etc.)
    short_text = models.TextField(blank=True, default='')
    # The title of this daily entry
    title = models.TextField()
    # The verse associated with this daily entry
    verse = models.TextField(blank=True, default='')
    # The body text associated with this daily entry
    body = models.TextField(blank=True, default='')
    # The short description for this daily entry, also used for text messages
    summary = models.TextField(blank=True, default='')
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
            return self.sequence_num

    def __str__(self):
        if self.short_text != '':
            return "%s: %s" % (self.short_text, self.title)
        else:
            return self.title


def lookup_entry(devotional, entry_id):
    if len(entry_id) > 0:
        try:
            id = int(entry_id)
        except ValueError:
            # Is not an int - Look up string value
            try:
                entry = devotional.entry_set.get(shortcut=entry_id)
            except Entry.DoesNotExist:
                return None
        else:
            # Is an int - Look up integer value
            try:
                entry = devotional.entry_set.get(sequence_num=entry_id)
            except Entry.DoesNotExist:
                return None

        return entry
    else:
        return None

