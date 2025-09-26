class UserModel:
    def __init__(self):
        self.users = {
            "eugenia": {"password": "1234", "token": "etew"},
            "tomas": {"password": "5678", "token": "vsae"},
        }

    def get_user(self, username):
        return self.users.get(username)