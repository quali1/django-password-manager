from manager.serializers import PSManagerSerializer
from .models import Profile, ProfileCategories
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = serializers.StringRelatedField()
    saved_passwords = PSManagerSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'category', 'pin', 'created', 'updated', 'saved_passwords']

    def validate_pin(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("PIN must be an integer")
        if len(value) < 4 or len(value) > 6:
            raise serializers.ValidationError("Pin must be between 4 and 6 characters long")
        return value


class UserProfileTokenSerializer(serializers.Serializer):
    class Meta:
        model = ProfileCategories
        fields = '__all__'
