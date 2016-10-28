from rest_framework import permissions
from django.contrib.auth.forms import UserCreationForm
from oauth.forms.profile import RegisterForm2
from oauth.models.profile import Profile

from oauth.serializers.profile import UserSerializer, ProfileSerializer

from django.views.generic.edit import CreateView


class CreateUserView(CreateView):
    model = Profile
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = ProfileSerializer

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/api-auth/login/'

    def get_context_data(self, **kwargs):
        return {
        'a_form': UserCreationForm,
        'b_form': RegisterForm2
        }
