from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate_pin(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("PIN must be an integer")
        if len(value) < 4 or len(value) > 6:
            raise serializers.ValidationError("Pin must be between 4 and 6 characters long")
        return value
