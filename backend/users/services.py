from manager.encryption import PasswordUserEncryption


def api_encrypt_profile_pin(serializer, user):
    pue = PasswordUserEncryption()

    pin = serializer.validated_data['pin']
    hashed_pin = pue.encrypt_password(pin)

    serializer.validated_data['user'] = user
    serializer.validated_data['pin'] = hashed_pin

    return serializer
