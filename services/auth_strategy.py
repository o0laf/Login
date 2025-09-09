from interfaces.i_auth import IAuthStrategy
from data.users import USERS
from utils.password_hasher import PasswordHasher

ph = PasswordHasher()

class AuthByUsername(IAuthStrategy):
    def authenticate(self, identifier, password):
        for user in USERS:
            if user.username == identifier and ph.verify_password(password, user.password_hashed):
                return user
        return None

class AuthByEmail(IAuthStrategy):
    def authenticate(self, identifier, password):
        for user in USERS:
            if user.email == identifier and ph.verify_password(password, user.password_hashed):
                return user
        return None