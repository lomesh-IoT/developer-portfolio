from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    github_link = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    repo_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
