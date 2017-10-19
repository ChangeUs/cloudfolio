from django.conf.urls import url
from main.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
