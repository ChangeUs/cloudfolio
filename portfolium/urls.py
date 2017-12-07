from django.conf.urls import url, include
from django.contrib import admin
from account.views import signin

urlpatterns = [
    url(r'^', include('main.urls', namespace='main')),
    url(r'^admin/', admin.site.urls),
    url(r'^portfolios/', include('portfolio.urls', namespace='portfolios')),
    url(r'^accounts/', include('account.urls', namespace='accounts')),
    url(r'^showboxs/', include('portfolio.urls', namespace='showboxs')),
]
