from dotenv import load_dotenv
import os

load_dotenv

USE_CACHE = os.getenv('USE_CACHE', True)
REDIS_URL = os.getenv("REDIS_URL", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASS = os.getenv("REDIS_PASS", None)