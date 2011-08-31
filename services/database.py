import environment
import pymongo
import constants

def get_database_connection():
	address, port = environment.get_database_serverinfo()
	return pymongo.Connection(address, port)

def get_database():
	return get_database_connection()[constants.DATABASE_NAME]
	
	
	
