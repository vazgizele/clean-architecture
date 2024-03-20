from dataclasses import dataclass
import os

@dataclass
class DbConfig():
    db_path: str
    db_echo: str
    db_timeout: str

    def __init__(self):
        db_host = os.environ.get('DB_HOST', '') # "localhost"
        db_name = os.environ.get('DB_NAME', '') # "tmo"
        db_user = os.environ.get('DB_USER', '') # "kobe"
        db_password = os.environ.get('DB_PASSWORD', '') # "kobewan"
        db_driver=os.environ.get('DB_DRIVER', '')

        self.db_path = f"{db_driver}://{db_user}:{db_password}@{db_host}:5432/{db_name}"
        self.db_echo = os.environ.get('DB_ECHO', '')
        self.db_timeout = os.environ.get('DB_TIMEOUT', 0)