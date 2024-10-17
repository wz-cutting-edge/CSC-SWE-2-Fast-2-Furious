# feed/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField(default=dict)

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content_type = models.CharField(max_length=50)
    metadata = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)