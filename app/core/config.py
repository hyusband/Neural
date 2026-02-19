from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    GROQ_API_KEY: str
    NOTION_TOKEN: str
    NOTION_DATABASE_ID: str
    SQLITE_DB_PATH: str = "neural.db"
    
    SAMPLE_RATE: int = 16000
    CHANNELS: int = 1
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
