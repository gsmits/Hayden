import environment
import pymongo
import constants

_cached_database = None

def get_database_connection():
	address, port = environment.get_database_serverinfo()
	return pymongo.Connection(address, port)

def get_database():
	global _cached_database
	if _cached_database is None:
		_cached_database = get_database_connection()[constants.DATABASE_NAME]
	return _cached_database

def get_domain(domain_name):
	return get_database()[domain_name]
	
	
	
