from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_reset
from account.views import signup

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    # default로 registration/login.html(logout.html)을 render
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]
