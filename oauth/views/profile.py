from rest_framework import generics
from oauth.models import Profile
from oauth.serializers import ProfileSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.views import generic
from django.contrib.auth.models import User
from rest_framework.response import Response

class HomeView(generic.TemplateView):
    template_name = 'home.html'


class ProfileListView(generic.ListView):
    model = User
    template_name = 'profile_list.html'


class ProfileDetailView(generic.DeleteView):
    model = User
    template_name = 'profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        context.update({
            'user': self.object
        })
        print self.object
        return context

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ListEndpoint(ProtectedResourceView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class DetailEndpoint(ProtectedResourceView):
    def get(self, request, format=None):
        """
        Return user details
        """
        user = Profile.objects.all().filter(self.request.user)
        return Response(user)



