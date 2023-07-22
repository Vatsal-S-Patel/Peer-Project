from django.db import models
from django.contrib.auth.models import User

import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    intro = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=180, null=True, blank=True)
    social_twitter = models.CharField(max_length=180, null=True, blank=True)
    social_linkedin = models.CharField(max_length=180, null=True, blank=True)
    social_youtube = models.CharField(max_length=180, null=True, blank=True)
    social_website = models.CharField(max_length=180, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return str(self.user.username)
        return str(self.username)
    

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


