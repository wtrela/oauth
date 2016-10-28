from django.contrib import admin

from oauth.views.profile import HomeView, ProfileListView, ProfileDetailView, \
    ListEndpoint, DetailEndpoint
from oauth.views.register import CreateUserView
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', view = HomeView.as_view()),
    url(r'^admin/', view =  admin.site.urls),

    # Registration of new users
    url(r'^register/$', view = CreateUserView.as_view(), name='register'),

    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),


    url(r'^profile/', include([
        url(r'^$', view = ProfileListView.as_view(), name='profile_list'),
        url(r'^(?P<pk>\d+)/', include([
                url(r'^$', view = ProfileDetailView.as_view(), name='profile_detail'),
            ])),
        ])),

    url(r'^profile/details/$', DetailEndpoint.as_view()),
    url(r'^profile/list/$', ListEndpoint.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
