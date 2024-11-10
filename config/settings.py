from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    mongo_uri: str = os.getenv("MONGO_URI")
    comunio_password: str = os.getenv("COMUNIO_PASSWORD")
    comunio_user: str = os.getenv("COMUNIO_USER")
    

settings = Settings()