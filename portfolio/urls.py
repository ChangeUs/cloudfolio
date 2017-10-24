from django.conf.urls import url
from portfolio.views import *

urlpatterns = [
    # TODO: url 백단에서 수정필요.
    # 프론트엔드를 위한 임시.
    url(r'^index/$', portfolioIndexView, name='index'),
    url(r'^base/$', portfolioBaseView, name='base'),
    url(r'^(?P<pk>[0-9]+)/$', portfolio_main_view, name='portfolio_main_view'),

    url(r'^profile/$', ProfileView.as_view(), name='portfolio_profile'),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfilePublicView.as_view(), name='portfolio_public_view'),
    url(r'^profile/edit$', ProfileEditView.as_view()),

    # 임시
    url(r'^activity/$', activity, name='activity'),
    url(r'^activity_edit/$', activity_edit, name='activity_edit'),
    url(r'^activity/create/(?P<tab_id>[0-9]+)/$', ActivityCreateView.as_view(), name='activity_create'),
    url(r'^activity/delete/(?P<activity_id>[0-9]+)/$', ActivityDeleteView.as_view(), name='activity_delete'),
    url(r'^story/create/(?P<activity_id>[0-9]+)/$', StoryCreateView.as_view(), name='story_create'),
    url(r'^story/delete/(?P<story_id>[0-9]+)/$', StoryDeleteView.as_view(), name='story_delete'),
    url(r'^tab/$', tab, name='tab'),
    url(r'^story_edit/$', story_edit, name='story_edit'),

]
