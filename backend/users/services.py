from manager.encryption import PasswordUserEncryption
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

def api_encrypt_profile_pin(serializer, user):
    pue = PasswordUserEncryption()

    pin = serializer.validated_data['pin']
    hashed_pin = pue.encrypt_password(pin)

    serializer.validated_data['user'] = user
    serializer.validated_data['pin'] = hashed_pin

    return serializer


def get_user_from_token(request):
    token_key = request.COOKIES.get('session_token')
    token = get_object_or_404(Token, key=token_key)
    return token.user