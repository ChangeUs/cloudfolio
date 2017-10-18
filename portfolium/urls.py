from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^portfolios/', include('portfolio.urls', namespace='portfolios')),
    url(r'^accounts/', include('account.urls', namespace='accounts')),
]
