class AuthService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def login(self, identifier, password):
        user = self.strategy.authenticate(identifier, password)
        if user:
            return f"✅ Bienvenido {user.username}"
        return "❌ Usuario o contraseña incorrectos"
