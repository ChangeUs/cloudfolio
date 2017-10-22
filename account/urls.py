from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from account.views import signup, delete_user, signin, activate

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^delete/$', delete_user, name='delete_user'),

    # default로 registration/login.html(logout.html)을 render
    url(r'^login/$', signin, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
]
