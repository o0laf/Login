class LoginView:
    def get_credentials(self):
        username = input("Usuario: ")
        credential = input("Contraseña/Token: ")
        return username, credential

    def show_result(self, success):
        if success:
            print("✅ Login exitoso")
        else:
            print("❌ Login fallido")