from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nume utilizator", max_length=100)
    password1 = forms.CharField(label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma parola", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')