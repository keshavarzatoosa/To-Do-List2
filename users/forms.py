from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2','name')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'


class CustomUserLoginForm(AuthenticationForm):
    name = forms.CharField(max_length=30)

    # class Meta(UserChangeForm.Meta):
    #     model = CustomUser
    #     fields = ('email', 'password','name')