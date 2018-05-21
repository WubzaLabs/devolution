from django.urls import path
from .views import devotionals


app_name = 'devolution'

urlpatterns = [
    # ex: /polls/
    path('', devotionals.devotionals, name='index'),
    # ex: /polls/40days/
    path('<str:devo_id>/', devotionals.title_page, name='title'),
    # ex: /polls/40days/contents/
    path('<str:devo_id>/contents/', devotionals.table_of_contents, name='contents'),
    # ex: /polls/40days/day1/
    path('<str:devo_id>/<str:entry_id>/', devotionals.entry, name='entry'),
]
