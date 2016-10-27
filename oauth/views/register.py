from rest_framework import permissions

from oauth.forms.profile import RegisterForm1, RegisterForm2
from oauth.models.profile import Profile

from oauth.serializers.profile import UserSerializer

from django.views.generic.edit import CreateView


class CreateUserView(CreateView):
    model = Profile
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    template_name = 'register.html'
    form_class = RegisterForm1
    success_url = '/api-auth/login/'

    def get_context_data(self, **kwargs):
        return {
        'a_form': RegisterForm1,
        'b_form': RegisterForm2
        }
