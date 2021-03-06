from oauth.models.profile import Profile
from django import forms


class RegisterForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address']

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s <br> %(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)