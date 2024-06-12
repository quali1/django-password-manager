from manager.encryption import PasswordUserEncryption
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


def api_encrypt_profile_pin(serializer, user):
    pue = PasswordUserEncryption()

    pin = serializer.validated_data['pin']
    hashed_pin = pue.encrypt_password(pin)

    serializer.validated_data['user'] = user
    serializer.validated_data['pin'] = hashed_pin

    return serializer


def get_user_from_token(request):
    token_key = request.COOKIES.get('session_token')
    token = Token.objects.get(key=token_key)

    if not token:
        return Response({'error': 'Provided token is incorrect.'}, status=status.HTTP_403_FORBIDDEN)

    return token.user