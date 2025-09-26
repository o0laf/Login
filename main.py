from controllers.login_controller import LoginController
from domain.models.user_model import UserModel
from domain.builders.user_builder import UserBuilder
from views.login_view import LoginView
from services.password_auth import PasswordAuth
from services.token_auth import TokenAuth

if __name__ == "__main__":
    model = UserModel()
    view = LoginView()

    # Elegí la estrategia que quieras
    strategy = PasswordAuth()   # o TokenAuth()

    controller = LoginController(model, view, strategy)
    controller.login()