# portfolio/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    user = models.ForeignKey('portfolio.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, default="Not specified")

    def __str__(self):
        return self.title
