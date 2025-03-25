from extensions.database import mongo
from models.user import User
from serializers.user_serializer import UserSerializer


class UserRepository:

    @staticmethod
    def register(user: User):
        serialized_user = UserSerializer.serialize_user(user)
        mongo.db.users.insert_one(serialized_user)
        return serialized_user

    @staticmethod
    def find_by_email(email):
        user=mongo.db.users.find_one({"email": email})
        if user is None:
            return None
        else: UserSerializer.deserialize_user(user)
