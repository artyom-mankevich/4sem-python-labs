import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30, min_length=3,
                               help_text="Latin lowercase letters, underscores and digits only. At least 3 "
                                         "characters.")
    email = forms.EmailField(required=True, validators=[EmailValidator(message="Email is invalid")])
    first_name = forms.CharField(required=False, help_text="First letter should be uppercase. Only latin characters. "
                                                           "Example: John.")
    last_name = forms.CharField(required=False, help_text="First letter should be uppercase. Only latin characters. "
                                                          "Example: Smith.")

    def clean_username(self):
        data = self.cleaned_data['username']
        if not re.match("^[a-z0-9_]{3,30}$", data):
            raise ValidationError("Username is invalid")
        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if data and not re.match("^[A-Z][a-z]+$", data):
            raise ValidationError("First name is invalid")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if data and not re.match("^[A-Z][a-z]+$", data):
            raise ValidationError("Last name is invalid")
        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
