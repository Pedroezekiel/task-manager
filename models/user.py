import uuid
import bcrypt


class User:

    def __init__(self, name, email, password):
        self._id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = self.hash_password(password)


    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


    def verify_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def get_id(self):
        return self._id
