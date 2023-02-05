from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from phonenumber_field.formfields import PhoneNumberField
# from django.utils.translation import ugettext_lazy as _

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address')
    name = forms.TextInput()
    # phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # label = {
        #     'first_name': _('email-address'),
        # }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    # phone_number = PhoneNumberField()

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location',  'public_email','facebook_link', 'twitter_link',
                  'whats_app_link', 'instagram_link']
