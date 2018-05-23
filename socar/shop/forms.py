from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserForm(UserCreationForm):
    pass


class User(AuthenticationForm):
    pass