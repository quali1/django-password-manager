from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SavedPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='saved_passwords')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    key = models.CharField(max_length=256)
    website = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website
