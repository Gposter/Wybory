from django import forms
from .models import osoba_gl
class LoginForm(forms.Form):
    pesel=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)





