import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI DDD Hexagonal")
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "mydatabase")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")

settings = Settings()