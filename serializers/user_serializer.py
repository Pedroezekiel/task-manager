import serializers
from models.user import User


class UserSerializer:
    @staticmethod
    def serialize_user(user: User):
        return {
            "_id":user.get_id(),
            "name":user.name,
            "email":user.email,
            "password":user.password
        }

    @staticmethod
    def deserialize_user(serialized_user: dict):
        return {
            "_id":serialized_user["_id"],
            "name":serialized_user["name"],
            "email":serialized_user["email"],
        }