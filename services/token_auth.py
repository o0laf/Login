from services.auth_strategy import AuthStrategy

class TokenAuth(AuthStrategy):
    def authenticate(self, user, token) -> bool:
        return user.token == token