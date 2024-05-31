import bcrypt
from cryptography.fernet import Fernet


class PasswordUserEncryption:

    @staticmethod
    def encrypt_password(password: str) -> bytes:
        """
        Hashing password using salt
        :param password: User password
        :return: Hashed password
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    @staticmethod
    def check_password(input_password, hashed_password) -> bool:
        """
        Checking password
        :param input_password:
        :param hashed_password:
        :return: Is password valid
        """
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)


class PasswordManagerEncryption:

    @staticmethod
    def encrypt_password(password: str) -> tuple:
        """
        Encrypts a password using Fernet.

        :param password: The password to encrypt.
        :return: A tuple containing the encrypted password and the encryption key.
        """
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_password = cipher.encrypt(password.encode())
        return encrypted_password.decode('utf-8'), key.decode('utf-8')

    @staticmethod
    def decrypt_password(encrypted_password: str, key: str) -> str:
        """
        Decrypts an encrypted password using Fernet.

        :param encrypted_password: The encrypted password to decrypt.
        :param key: The encryption key.
        :return: The decrypted password.
        """
        encrypted_password = bytes(encrypted_password, 'utf-8')
        key = bytes(key, 'utf-8')
        cipher = Fernet(key)
        decrypted_password = cipher.decrypt(encrypted_password).decode()
        return decrypted_password


if __name__ == '__main__':
    password = 'passwrord'
    pm = PasswordManagerEncryption()
    encrypted_tuple = pm.encrypt_password(password)
    print('Encrypted password and key:', encrypted_tuple)

    decrypted_password = pm.decrypt_password(encrypted_tuple[0], encrypted_tuple[1])
    print('Decrypted password:', decrypted_password)
