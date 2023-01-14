
from django.core import validators
from django import forms
from enroll.models import User


class Studentregistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']

        widgets = {
              'name' : forms.TextInput(attrs={'class':'form-control'}),
              'email' : forms.EmailInput(attrs={'class':'form-control'}),
              'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }