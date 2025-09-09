import bcrypt

class PasswordHasher:
    def hash_password(self, plain_password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plain_password.encode(), salt).decode()

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())