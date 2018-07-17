from .models import *
from django import forms
from django.contrib.auth.models import User


class Reg_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("the two password fields did not match. ")
            return self.cleaned_data
    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

class cart(forms.ModelForm):
    about=forms.CharField(widget=forms.TextInput(),required=False)
    class Meta:
        model=Cart
        fields=['quantity']

class ord(forms.ModelForm):
    class Meta:
        model=Ord
        fields='__all__'

class cust(forms.ModelForm):
    class Meta:
        model=Cust
        fields='__all__'        
