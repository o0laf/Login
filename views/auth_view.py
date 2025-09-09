class AuthView:
    def show_menu(self):
        print("=== SISTEMA DE LOGIN ===")
        print("1. Iniciar sesión con username")
        print("2. Iniciar sesión con email")
        return input("Seleccione opción: ")

    def get_credentials(self):
        identifier = input("Ingrese username o email: ")
        password = input("Ingrese contraseña: ")
        return identifier, password

    def show_result(self, message):
        print(message)
