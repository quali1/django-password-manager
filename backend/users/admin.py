from django.contrib import admin
from .models import Profile, ProfileCategories, UserProfileToken

# Register your models here.

admin.site.register(Profile)
admin.site.register(ProfileCategories)
admin.site.register(UserProfileToken)