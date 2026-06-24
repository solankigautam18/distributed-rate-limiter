import time


def token_bucket(
    redis_client,
    key: str,
    capacity: int = 10,
    refill_rate: int = 1
):
    current_time = time.time()

    bucket = redis_client.hgetall(key)

    if not bucket:
        redis_client.hset(
            key,
            mapping={
                "tokens": capacity - 1,
                "last_refill": current_time
            }
        )

        redis_client.expire(key, 3600)

        return True

    tokens = float(bucket["tokens"])
    last_refill = float(bucket["last_refill"])

    elapsed = current_time - last_refill

    tokens = min(
        capacity,
        tokens + elapsed * refill_rate
    )

    if tokens < 1:
        redis_client.hset(
            key,
            mapping={
                "tokens": tokens,
                "last_refill": current_time
            }
        )

        return False

    tokens -= 1

    redis_client.hset(
        key,
        mapping={
            "tokens": tokens,
            "last_refill": current_time
        }
    )

    return True