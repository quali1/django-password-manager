from rest_framework import serializers
from .models import SavedPassword
from .encryption import PasswordManagerEncryption


class PSManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPassword
        read_only_fields = ('user',)
        write_only_fields = ('key',)
        fields = ['user', 'profile', 'password', 'website', 'note', 'created', 'updated']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'password' in representation:
            pse = PasswordManagerEncryption()
            key = instance.key
            password = instance.password
            decrypted_password = pse.decrypt_password(password, key)
            representation['password'] = decrypted_password
        return representation
