class User:
    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token


class UserBuilder:
    def __init__(self):
        self.username = None
        self.password = None
        self.token = None

    def set_username(self, username):
        self.username = username
        return self

    def set_password(self, password):
        self.password = password
        return self

    def set_token(self, token):
        self.token = token
        return self

    def build(self):
        return User(self.username, self.password, self.token)