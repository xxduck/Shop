# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from django import forms
# from .models import MyUser


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ['username', "passwd1"]


# class UserRegist(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ['username', 'passwd1', 'passwd2', 'nick']

# class CreateUser(UserCreationForm):
#     pass


class MyForm(forms.Form):
    tel = forms.CharField(label="电话号码",max_length=12)

    def clean(self):
        tel = self.cleaned_data.get("tel")
        print(tel)
        if tel == "15732633601":
            print("success")
            return self.cleaned_data
        else:
            raise forms.ValidationError("电话号码有误")