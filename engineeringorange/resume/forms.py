from django import forms
from resume.models import Accounts, Jobseeker
from django.contrib.auth.models import User

class RegistrationForm (forms.Form):
    firstName = forms.CharField(label='First Name')
    lastName = forms.CharField(label='Last Name')
    email = forms.EmailField(label='E-mail')
    username = forms.IntegerField(label='Student Number')
    password = forms.CharField(widget=forms.PasswordInput)
    
class LogInForm (forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')