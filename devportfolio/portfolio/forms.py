from django import forms
from .models import Project, User

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['resume']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'repo_link']
