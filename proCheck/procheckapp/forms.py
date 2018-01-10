from django import forms
from procheckapp import models
from procheckapp.models import UserDetailsInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'password')

class UserDetailsInfoForm(forms.ModelForm):
    class Meta():
        model = UserDetailsInfo
        fields = ('email', 'phone')
