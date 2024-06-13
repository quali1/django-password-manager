from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=20)
    pin = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID: {self.id} {self.name} -- {self.user}'


class UserProfileToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_token')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_token', related_query_name='token')
    key = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.profile}"
