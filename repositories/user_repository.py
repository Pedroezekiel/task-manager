from extensions.database import mongo_tasks as mongo
from models.user import User
from serializers.user_serializer import UserSerializer


class UserRepository:

    @staticmethod
    def register(user: User):
        serialized_user = UserSerializer.serialize_user(user)
        mongo.db.users.insert_one(serialized_user)
        serialized_user.pop("password")
        return serialized_user

    @staticmethod
    def find_by_email(email):
        user=mongo.db.users.find_one({"email": email})
        print(type(user))
        if user is None:
            return None
        else: return User(
            name=user["name"],
            email=user["email"],
            password=user["password"]  # This should already be hashed
        )
