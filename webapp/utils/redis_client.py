from functools import lru_cache
from redis import Redis


@lru_cache(maxsize=None)
def get_redis_client():
    redis_client: Redis = Redis(host="redis", port=6379)
    return redis_client
