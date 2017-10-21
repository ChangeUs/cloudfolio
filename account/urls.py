from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_reset
from account.views import signup, signin, delete_user

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    # default로 registration/login.html(logout.html)을 render
    url(r'^login/$', signin, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^delete/$', delete_user, name='delete_user'),
]
