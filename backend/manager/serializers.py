from rest_framework import serializers
from .models import SavedPassword
from .encryption import PasswordManagerEncryption


class PSManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPassword
        read_only_fields = ('user', 'key')
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'password' in representation:
            pse = PasswordManagerEncryption()
            key = representation['key']
            password = representation['password']
            decrypted_password = pse.decrypt_password(password, key)
            representation['decrypted_password'] = decrypted_password
        return representation
