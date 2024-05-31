from .encryption import PasswordManagerEncryption


def api_encrypt_password(serializer, user):
    pme = PasswordManagerEncryption()
    password = serializer.validated_data['password']
    password, key = pme.encrypt_password(password)

    serializer.validated_data['user'] = user
    serializer.validated_data['password'] = password
    serializer.validated_data['key'] = key

    return serializer