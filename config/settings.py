from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    mongo_uri: str = os.getenv("MONGO_URI")

settings = Settings()