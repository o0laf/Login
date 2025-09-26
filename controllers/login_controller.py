class LoginController:
    def __init__(self, model, view, strategy):
        self.model = model
        self.view = view
        self.strategy = strategy

    def login(self):
        username, credential = self.view.get_credentials()
        data = self.model.get_user(username)

        if not data:
            self.view.show_result(False)    
            return

        user = type("User", (), data)

        success = self.strategy.authenticate(user, credential)
        self.view.show_result(success)