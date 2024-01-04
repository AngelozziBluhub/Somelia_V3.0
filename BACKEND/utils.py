from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

# Not clear if it is a recursive call... I've no idea on what's going on here...