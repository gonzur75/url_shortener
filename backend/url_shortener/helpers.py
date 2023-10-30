import secrets
import string


def token_handler():
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for i in range(8))
    return token
