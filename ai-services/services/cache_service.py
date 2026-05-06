import redis
import json
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

# Redis connection
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_TTL = 900  # 15 minutes in seconds


def get_redis_client():
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            socket_connect_timeout=2
        )
        # Test connection
        client.ping()
        return client
    except Exception as e:
        print(f"Redis connection failed: {e}")
        return None


def make_cache_key(endpoint: str, text: str) -> str:
    # Create SHA256 hash of endpoint + text
    raw = f"{endpoint}:{text}"
    return hashlib.sha256(raw.encode()).hexdigest()


def get_from_cache(endpoint: str, text: str):
    try:
        client = get_redis_client()
        if client is None:
            return None

        key = make_cache_key(endpoint, text)
        cached = client.get(key)

        if cached:
            print(f"Cache HIT for {endpoint}")
            data = json.loads(cached)
            data["cached"] = True
            return data

        print(f"Cache MISS for {endpoint}")
        return None

    except Exception as e:
        print(f"Cache get error: {e}")
        return None


def set_in_cache(endpoint: str, text: str, data: dict):
    try:
        client = get_redis_client()
        if client is None:
            return False

        key = make_cache_key(endpoint, text)
        client.setex(
            key,
            CACHE_TTL,
            json.dumps(data)
        )
        print(f"Cached response for {endpoint}")
        return True

    except Exception as e:
        print(f"Cache set error: {e}")
        return False


def get_cache_stats():
    try:
        client = get_redis_client()
        if client is None:
            return {
                "status": "unavailable",
                "message": "Redis not connected"
            }

        info = client.info()
        return {
            "status": "connected",
            "used_memory": info.get("used_memory_human", "unknown"),
            "connected_clients": info.get("connected_clients", 0),
            "total_keys": client.dbsize()
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }