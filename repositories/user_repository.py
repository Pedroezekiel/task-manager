from extensions.database import mongo_users as mongo
from models.user import User
from serializers.user_serializer import UserSerializer


class UserRepository:

    @staticmethod
    def save(user: User):
        serialized_user = UserSerializer.serialize_user(user)
        mongo.db.users.insert_one(serialized_user)
        serialized_user.pop("password")
        return serialized_user

    @staticmethod
    def find_by_email(email):
        user_data=mongo.db.users.find_one({"email": email})
        print(type(user_data))
        print(user_data)
        if user_data is None:
            return None
        else:
            user = User(
            name=user_data["name"],
            email=user_data["email"],
            password=user_data["password"])
            user.set_id(user_data["_id"])
            return user


    @staticmethod
    def find_user_name_by_id(id):
        print(id)
        print(id)
        user=mongo.db.users.find_one({"_id": id})
        print(user)
        return user["name"]
