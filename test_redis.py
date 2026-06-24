from app.redis_client import redis_client

redis_client.set("name", "gautam")

print(redis_client.get("name"))