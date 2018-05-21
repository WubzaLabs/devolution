from django.contrib import admin
from .models.devotional import Devotional
from .models.entry import Entry
from .models.subscription import Subscription
from .models.user import User


# Register your models here.
admin.site.register(Devotional)
admin.site.register(Entry)
admin.site.register(Subscription)
admin.site.register(User)
