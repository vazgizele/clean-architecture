from dotenv import load_dotenv

from src.infra.adapters.db_config.db_config import DbConfig

if __name__ == 'main':
    load_dotenv()
    db_config = DbConfig()