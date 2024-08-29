from pymongo import MongoClient
from settings import DB_URL

client = MongoClient(DB_URL)

test_db = client.test

users_db = test_db.users
tickets_db = test_db.tickets