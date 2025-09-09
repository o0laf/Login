from services.auth_service import AuthService
from services.auth_strategy import AuthByUsername, AuthByEmail
from views.auth_view import AuthView

class AuthController:
    def __init__(self):
        self.view = AuthView()

    def login(self):
        option = self.view.show_menu()
        identifier, password = self.view.get_credentials()

        strategy = AuthByUsername() if option == "1" else AuthByEmail()
        auth_service = AuthService(strategy)

        result = auth_service.login(identifier, password)
        self.view.show_result(result)