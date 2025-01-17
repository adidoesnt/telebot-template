import os
from dotenv import load_dotenv

load_dotenv()

# Environment
ENV = os.getenv("ENV", "dev")

# Server
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Telegram
BOT_TOKEN=os.getenv("BOT_TOKEN")

# Database
DB_NAME = os.getenv("DB_NAME", "test_db")
DB_USER = os.getenv("DB_USER", "test_user")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
# DB_PATH = os.getenv("DB_PATH")
