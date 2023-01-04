from hashlib import sha512

class Hash():
    def hash_pass(password: str):
        return sha512(password.encode()).hexdigest()

    def verify(hashed_password, plain_password):
        return hashed_password == sha512(plain_password.encode()).hexdigest()