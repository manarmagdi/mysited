
from django import forms
from django.contrib.auth.forms import AuthenticationForm 


class LogInForm(forms.Form):
    Email = forms.CharField(label='Email', max_length=50)
    Password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)


