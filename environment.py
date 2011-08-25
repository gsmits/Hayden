import constants
import os

TP_ENVIRON_VAR="HAYDEN_ENVIRONMENT"

TP_ENVIRON_PRODUCTION="prod"
TP_ENVIRON_DEVELOPMENT="dev"
TP_ENVIRON_DEFAULT=TP_ENVIRON_DEVELOPMENT

def get_environment():
	return os.environ.get(TP_ENVIRON_VAR, TP_ENVIRON_DEFAULT) 


def is_production():
	return get_environment() == TP_ENVIRON_PRODUCTION	


def is_development():
	return get_environment() == TP_ENVIRON_DEVELOPMENT

def get_app_server():
	hosts = {
		TP_ENVIRON_PRODUCTION: "www.pingu.com",
		TP_ENVIRON_DEVELOPMENT: "localhost:8888",
	}
	environment = get_environment()
	return hosts[environment]

def get_api_server():
	hosts = {
		TP_ENVIRON_PRODUCTION: "api.pingu.com",
		TP_ENVIRON_DEVELOPMENT: "localhost:8001",
	}
	environment = get_environment()
	return hosts[environment]


def get_database_serverinfo():
	conninfo = {
		TP_ENVIRON_PRODUCTION: ("?", 27017),
		TP_ENVIRON_DEVELOPMENT: ("127.0.0.1", 27017),
	}
	environment = get_environment()
	return conninfo[environment]
	