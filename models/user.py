class User:
    def __init__(self, username, email, password_hashed):
        self.username = username
        self.email = email
        self.password_hashed = password_hashed

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"

class UserBuilder:
    def __init__(self):
        self.username = None
        self.email = None
        self.password_hashed = None

    def set_username(self, username):
        self.username = username
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_password_hashed(self, password_hashed):
        self.password_hashed = password_hashed
        return self

    def build(self):
        return User(self.username, self.email, self.password_hashed)