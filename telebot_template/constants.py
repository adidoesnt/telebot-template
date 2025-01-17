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
