from utils.password_hasher import PasswordHasher
from models.user import UserBuilder

ph = PasswordHasher()

USERS = [
    UserBuilder()
        .set_username("olaf")
        .set_email("olaf@gmail.com")
        .set_password_hashed(ph.hash_password("1234"))
        .build(),
    UserBuilder()
        .set_username("maria")
        .set_email("maria@gmail.com")
        .set_password_hashed(ph.hash_password("2345"))
        .build()
]