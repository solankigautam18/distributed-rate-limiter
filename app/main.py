from fastapi import FastAPI

from app.redis_client import redis_client
from app.limiter import token_bucket

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Rate Limiter Running"}


@app.get("/check")
def check(user_id: str):

    allowed = token_bucket(
        redis_client,
        f"user:{user_id}"
    )

    return {
        "user": user_id,
        "allowed": allowed
    }