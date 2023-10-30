from logging import INFO, ERROR, WARNING, DEBUG
import sys
import os

def is_environment_param():
    return len(sys.argv)>1 and str(sys.argv) in ["development","production"]

APP_NAME="henry_steam_api"
ENVIRONMENT_MODE = str(str(sys.argv[1]) if is_environment_param() else os.environ.get(f"{APP_NAME}".upper()+"_ENVIRONMENT_MODE", "development")).upper()

NO_MOSTRAR = ["DEBUG_MODE","LOG_LEVEL","DIRECTORIO_LOGS"]

DEVELOPMENT = {
    "DEBUG_MODE": True,
    "PYTHON_HOST": "0.0.0.0",
    "PYTHON_PORT":  5000,
    "API_BASE_PATH": "/api",
    "LOG_LEVEL": DEBUG,
    "DIRECTORIO_LOGS": "./logs",
    "ENV": ENVIRONMENT_MODE
}
PRODUCTION = {
    "DEBUG_MODE": False,
    "PYTHON_HOST": "0.0.0.0",
    "PYTHON_PORT":  5000,
    "API_BASE_PATH": "/api",
    "LOG_LEVEL": INFO,
    "DIRECTORIO_LOGS": "./logs",
    "ENV": ENVIRONMENT_MODE
}

