"""oauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin

from oauth.views.profile import ProfileList, ProfileDetails
from oauth.views.registration import RegistrationView
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Registration of new users
    url(r'^register/$', RegistrationView.as_view()),

    url(r'^profile/details/$', ProfileDetails.as_view()),
    url(r'^profile/list/$', ProfileList.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace = 'oauth2_provider'),)
]
