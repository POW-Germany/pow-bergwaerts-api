import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to manage environment variables."""

    @staticmethod
    def get(key: str, default=None):
        """Get the value of an environment variable."""
        return os.getenv(key, default)

    @staticmethod
    def get_int(key: str, default=0):
        """Get the value of an environment variable as an integer."""
        try:
            return int(os.getenv(key, default))
        except ValueError:
            return default

    @staticmethod
    def get_bool(key: str, default=False):
        """Get the value of an environment variable as a boolean."""
        return os.getenv(key, str(default)).lower() in ("true", "1", "yes")

    APP_NAME = get("APP_NAME", "FastAPI Application")
    APP_VERSION = get("APP_VERSION", "1.0.0")
    LOG_LEVEL = get("LOG_LEVEL", "DEBUG")
    DATABASE_URL = get("DATABASE_URL", "sqlite:///./test.db")
