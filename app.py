from services.auth_service import AuthService
from services.auth_strategy import AuthByUsername, AuthByEmail

def main():
    print("=== SISTEMA DE LOGIN ===")
    print("1. Iniciar sesión con username")
    print("2. Iniciar sesión con email")
    option = input("Seleccione opción: ")

    identifier = input("Ingrese username o email: ")
    password = input("Ingrese contraseña: ")

    # Seleccionar estrategia de autenticación
    strategy = AuthByUsername() if option == "1" else AuthByEmail()
    auth_service = AuthService(strategy)

    # Intentar login
    print(auth_service.login(identifier, password))

if __name__ == "__main__":
    main()