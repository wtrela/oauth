from rest_framework import generics
from oauth.models import Profile
from oauth.serializers import ProfileSerializer, SignUpSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http.response import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from oauth.permissions import IsAuthenticatedOrCreate

class HomeView(generic.TemplateView):
    template_name = 'index.html'

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Protected with OAuth2!')


###### dorobione

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)