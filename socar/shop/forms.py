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


class BuyForm(forms.Form):
    # 购买界面的表单
    num = forms.IntegerField(label="数量", max_value=10, min_value=0)
    colour = forms.ChoiceField(label="颜色", choices=(
       (1, "黑色"),
       (2, "红色"),
       (3, "紫色"),
    ))
    size = forms.ChoiceField(label="尺码", choices=(
        (1, "M"),
       (2, "L"),
       (3, "XL"),
    ))