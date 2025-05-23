# portfolio/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project  # your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies']
