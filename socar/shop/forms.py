from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import MyUser


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', "passwd1"]


class UserRegist(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'passwd1', 'passwd2', 'nick']
