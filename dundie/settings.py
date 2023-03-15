import os

SMTP_HOST = "localhost"
SMTP_PORT = 8025
SMTP_TIMEOUT = 5
EMAIL_FROM = "master@dundie.com"

ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, "..", "assets", "database.db")

SQL_CON_STRING = f"sqlite:///{DATABASE_PATH}"

DATEFMT = "%d/%m/%Y %H:%M:%S"

API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"
