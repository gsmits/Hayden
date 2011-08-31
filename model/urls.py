
from services import database

def get_urls_by_user(user_name):
    return database.get_database().urls.find({"user_name": user_name})

def get_url_by_url(url):
    return database.get_database().urls.find({"url": url})

def insert(url, user_name):
    return database.get_database().urls.save({ "user_name" : user_name, "url" : url })

def log(url_id, response):
    return database.get_database().urls.save({ "url_id" : url_id, "response" : response })

def log_by_url(url, response):

    url = get_url_by_url(url)

    return database.get_database().urls.save({ "url_id" : url_id, "response" : response })
  