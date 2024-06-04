from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProfileCategories(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    category = models.ForeignKey(ProfileCategories, on_delete=models.CASCADE)
    pin = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.category} -- {self.user}'


class UserProfileToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_token')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_token')
    token = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.profile}"