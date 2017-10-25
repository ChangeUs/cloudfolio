from django.conf.urls import url
from account.views import signin
from main.views import *

urlpatterns = [
    url(r'^$', signin),
    url(r'^showbox/$', ShowboxView.as_view(), name='showbox'),
]
