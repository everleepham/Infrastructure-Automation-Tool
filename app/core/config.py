import os
from dotenv import load_dotenv
import redis

load_dotenv()

REDIS_URI = os.getenv('REDIS_URI', 'redis://localhost:6379/')

try:
    redis_client = redis.from_url(REDIS_URI)
    redis_client.ping()
    print("Redis connection established.")
except redis.RedisError as e:
    print("Redis connection failed:", e)

