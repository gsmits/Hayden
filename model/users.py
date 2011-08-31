
from services import database

def get_user(user_name):
    return database.get_database().users.find_one({ "user_name" : user_name })

def insert(user_name):
    return database.get_database().users.save({ "user_name" : user_name })
  