from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

