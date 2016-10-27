from django.forms import ModelForm
from django.contrib.auth.models import User
from oauth.models.profile import Profile

class RegisterForm1(ModelForm):
    class Meta:
        model = User

class RegisterForm2(ModelForm):
    class Meta:
        model = Profile