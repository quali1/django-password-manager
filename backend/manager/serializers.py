from rest_framework import serializers
from .models import SavedPassword
from .encryption import PasswordManagerEncryption


class PSManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedPassword
        read_only_fields = ('key', 'user')
        fields = '__all__'

