from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.views import password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from account.views import signup, signin, activate, change_password

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    # default로 registration/login.html(logout.html)을 render
    url(r'^login/$', signin, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),

    url(r'^password_change/$', change_password, name='password_change'),
    url(r'^password_change/done/$', password_change_done, name='password_change_done'),

    url(r'^password_reset/$', password_reset, {'post_reset_redirect': '/accounts/password_reset/done/'}, name="password_reset"),
    url(r'^password_reset/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'post_reset_redirect': '/accounts/reset/done/'}, name="password_reset_confirm"),
    url(r'^reset/done/$', password_reset_complete, name="password_reset_complete"),
]
