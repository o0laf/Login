from services.auth_strategy import AuthStrategy

class PasswordAuth(AuthStrategy):
    def authenticate(self, user, password) -> bool:
        return user.password == password