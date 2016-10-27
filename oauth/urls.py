from rest_framework import urls
from django.contrib import admin

from oauth.views.profile import ProfileList, ProfileDetails, ApiEndpoint, HomeView, SignUp
from oauth.views.registration import CreateUserView
from django.conf.urls import url, include

urlpatterns = [
    # url(r'^$', HomeView.as_view()),
    url(r'^$', ApiEndpoint.as_view()),
    url(r'^admin/', admin.site.urls),

    # Registration of new users
    url(r'^register/$', SignUp.as_view(), name='register'),



    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),


    url(r'^profile/details/$', ProfileDetails.as_view()),

    # url(r'^profile/details/$', ApiEndpoint.as_view()),
    url(r'^profile/list/$', ProfileList.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace = 'oauth2_provider'),)
]
