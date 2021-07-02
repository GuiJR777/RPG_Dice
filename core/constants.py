from dotenv import load_dotenv
import os

load_dotenv

USE_CACHE = os.getenv('USE_CACHE', True)
REDIS_URL = os.getenv("REDIS_URL", "//:pb0106841fca87bd35f7cf83914bda3b80923ac0e1313c3a50908f97ec27b68bb@ec2-52-45-192-3.compute-1.amazonaws.com:15099")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASS = os.getenv("REDIS_PASS", None)