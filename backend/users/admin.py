from django.contrib import admin
from .models import Profile, UserProfileToken

# Register your models here.

admin.site.register(Profile)
admin.site.register(UserProfileToken)