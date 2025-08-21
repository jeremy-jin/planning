import json
import pickle

from django.conf import settings
from django.core.cache import cache


class MemberRedisClient:
    def __init__(self, redis_client=None, **kwargs):
        self.redis_client = cache.client.get_client() if redis_client is None else redis_client
        self.time_out = (
            settings.CACHES.get("default", {}).get("OPTIONS", {}).get("TIMEOUT", 3600)
        )

    def encode(self, data: dict):
        return {k: json.dumps(v) for k, v in data.items()}

    def decode(self, data):
        return {k: json.loads(v) for k, v in data.items()}

    @staticmethod
    def encode_utf8(value):
        return value.decode("utf-8") if isinstance(value, bytes) else value

    def del_key(self, key):
        return cache.delete(key)

    def hdel(self, key):
        return self.redis_client.delete(key)

    def exists(self, key):
        return self.redis_client.exists(key)

    def hgetall(self, key):
        data = self.redis_client.hgetall(key)
        if not data:
            return None

        return {
            self.encode_utf8(k): self.encode_utf8(v)
            for k, v in self.decode(data).items()
        }

    def hset(self, key, mapping):
        pipe = self.redis_client.pipeline()
        pipe.hset(key, mapping=self.encode(mapping))
        pipe.expire(key, self.time_out)
        return pipe.execute()

    def hupdate(self, key, mapping):
        pipe = self.redis_client.pipeline()
        pipe.hset(key, mapping=self.encode(mapping))
        return pipe.execute()