from django.conf.urls import url
from portfolio.views import *

urlpatterns = [
    # TODO: url 백단에서 수정필요.
    # 프론트엔드를 위한 임시.
    url(r'^index/$', portfolioIndexView, name='index'),
    url(r'^base/$', portfolioBaseView, name='base'),
    url(r'^(?P<pk>[0-9]+)/$', portfolio_main_view, name='portfolio_main_view'),

    url(r'^profile/$', ProfileView.as_view(), name='portfolio_profile'),
    url(r'^profile/edit$', ProfileEditView.as_view()),

    # 임시
    url(r'^activity/$', activity, name='activity'),
    url(r'^activity_edit/$', activity_edit, name='activity_edit'),
    url(r'^tab/$', tab, name='tab'),
    url(r'^story_edit/$', story_edit, name='story_edit'),

]
