from django.contrib import admin

from oauth.views.profile import ProfileList, ProfileDetails, HomeView, ProfileView
from oauth.views.register import CreateUserView
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),

    # Registration of new users
    url(r'^register/$', CreateUserView.as_view(), name='register'),

    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    url(r'^profile/$', ProfileView.as_view()),
    url(r'^profile/details/$', ProfileDetails.as_view()),
    url(r'^profile/list/$', ProfileList.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace = 'oauth2_provider'),)
]
