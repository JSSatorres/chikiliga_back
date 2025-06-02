"""
Application configuration settings
"""
import os
from typing import List, Union
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Football Stats API"
    PROJECT_DESCRIPTION: str = "API to fetch football player stats from Comunio and Comuniazo"
    PROJECT_VERSION: str = "1.0.0"
    
    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    SESSION_COOKIE_MAX_AGE: int = 14 * 24 * 60 * 60  # 14 days in seconds
    
    # CORS settings
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8080",
    ]
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # Host security
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./comunio_project.db")
    
    # MongoDB settings
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DATABASE: str = os.getenv("MONGODB_DATABASE", "comunio_project")
    
    COMUNIO_USER: str = ""
    COMUNIO_PASSWORD: str = ""
    MONGO_USER: str = ""
    MONGO_PASSWORD: str = ""
    MONGO_URI: str = ""
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


def get_settings() -> Settings:
    """Get application settings instance"""
    return Settings()


settings = Settings()