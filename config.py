from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGO_URI_TASKS = os.getenv("DATABASE_URI_TASKS")
    MONGO_URI_USERS = os.getenv("DATABASE_URI_USERS")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]