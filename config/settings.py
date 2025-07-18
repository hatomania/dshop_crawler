import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    DEBUG = os.getenv("DEBUG", "False") == "True"

    DB_SERVER=os.getenv("DB_SERVER")
    DB_PORT=os.getenv("DB_PORT")
    DB_USERNAME=os.getenv("DB_USERNAME")
    DB_PASSWORD=os.getenv("DB_PASSWORD")
    DB_DBNAME=os.getenv("DB_DBNAME")

    BASE_URL=os.getenv("BASE_URL")

settings = Settings()
