from rest_framework import generics
from oauth.models import Profile
from oauth.serializers import ProfileSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http.response import HttpResponse

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Protected with OAuth2!')