from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_reset
from portfolio.views import *

urlpatterns = [
    # TODO: url 백단에서 수정필요.
    # 프론트엔드를 위한 임시.
    url(r'^index/$', portfolioIndexView, name='index'),
    url(r'^base/$', portfolioBaseView, name='base'),
    url(r'^(?P<pk>[0-9]+)/$', portfolio_main_view, name='portfolio_main_view'),
]
