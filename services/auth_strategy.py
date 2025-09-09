from interfaces.auth_interface import AuthStrategy
from data.users import USERS
from utils.password_hasher import PasswordHasher

ph = PasswordHasher()

class AuthByUsername(AuthStrategy):
    def authenticate(self, identifier, password):
        for user in USERS:
            if user.username.lower() == identifier.lower() and ph.verify_password(password, user.password_hashed):
                return user
        return None

class AuthByEmail(AuthStrategy):
    def authenticate(self, identifier, password):
        for user in USERS:
            if user.email.lower() == identifier.lower() and ph.verify_password(password, user.password_hashed):
                return user
        return None