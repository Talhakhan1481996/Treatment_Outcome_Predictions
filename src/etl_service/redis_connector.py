import redis  # type: ignore


def get_redis_client() -> redis.client.Redis:
    redis_host = "localhost"
    redis_port = 6379
    redis_db = 0
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    return redis_client

