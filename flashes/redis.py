import redis.asyncio as redis

from flashes import config

global_settings = config.Settings()

redis_conn: redis.Redis = None

async def init_redis_pool() -> redis.Redis:
    global redis_conn
    redis_conn = await redis.from_url(
        str(global_settings.redis_url),
        encoding="utf-8",
        db=global_settings.redis_db,
        decode_responses=True,
    )
    return redis_conn

async def close_redis_pool():
    global redis_conn
    await redis_conn.close()

async def get_redis() -> redis.Redis:
    return redis_conn

