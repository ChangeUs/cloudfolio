from django.conf.urls import url
from account.views import signin
from main.views import *

urlpatterns = [
    url(r'^$', signin),
    url(r'^showbox/$', ShowboxView.as_view(), name='showbox'),
    url(r'^resume/1/$', resume_sample_1, name='resume1'),
    url(r'^resume/2/$', resume_sample_2, name='resume2'),

]
