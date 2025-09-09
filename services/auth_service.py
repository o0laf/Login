class AuthService:
    def __init__(self, strategy):
        self.strategy = strategy  # Inyección de dependencia

    def login(self, identifier, password):
        user = self.strategy.authenticate(identifier, password)
        return f"✅ Bienvenido {user.username}" if user else "❌ Usuario o contraseña incorrectos"
