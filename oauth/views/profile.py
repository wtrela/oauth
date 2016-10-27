from rest_framework import generics
from oauth.models import Profile
from oauth.serializers import ProfileSerializer, SignUpSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http.response import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from oauth.permissions import IsAuthenticatedOrCreate
from django.utils import timezone

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class ProfileView(generic.ListView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        print kwargs
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['profile'] = User.objects.filter(username=self.request.user) # should be Profile
        return context



class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Protected with OAuth2!')
