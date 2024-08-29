import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
DB_URL = os.getenv("DB_URL")
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "role": "Admin",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

tickets = [
    {
    "ee_name": "johndoe",
    "email": "test@example.com",
    "issue": "not play this",
    "equipment": "CPU",
    "status": "Open"
    },
    {
    "ee_name": "johndoe",
    "email": "test@example.com",
    "issue": "not play this 2",
    "equipment": "CPU",
    "status": "Open"
    },
    {
    "ee_name": "johndoes",
    "email": "test@example.com",
    "issue": "not play this 2",
    "equipment": "CPU",
    "status": "Open"
    }
]