import orjson as json
from fastapi.responses import ORJSONResponse
from fastapi import FastAPI, Depends
from redis.asyncio import Redis
from flashes.redis import init_redis_pool, get_redis, close_redis_pool
from shortuuid import uuid
from flashes import fake
from typing import Annotated

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_redis_pool()

@app.on_event("shutdown")
async def shutdown_event():
    await close_redis_pool()

@app.get("/create_all/hash")
async def create_all_hash(redis: Annotated[Redis, Depends(get_redis)]):
    flashes_content: list[dict] = fake.get_all_flashes()
    keys = []
    for content in flashes_content:
        _key = uuid()
        keys.append(_key)
        await redis.hset(_key, mapping=content)
        await redis.rpush("user-1", _key)
    return keys

@app.get("/create_all/serialized/{id}", response_class=ORJSONResponse)
async def create_all_serialized(id: int, redis: Annotated[Redis, Depends(get_redis)]):
    flashes_content: list[dict] = fake.get_all_flashes(serialized=True)
    
    pipeline = redis.pipeline()
    for content in flashes_content:
        pipeline.rpush(f"user-{id}-serialized", content['msg'])

    await pipeline.execute()
    return ORJSONResponse({"key": f"user-{id}-serialized"})

def from_db_to_json(_from: dict) -> dict:
    return {
        "msg": _from["msg"],
        "key": _from["key"],
        "values": json.loads(_from["values"])
    }

def from_db_to_json_serialized(_from: str) -> dict:
    return json.loads(_from)

@app.get("/user/{id}/flash")
async def get_messages(id: int, redis: Annotated[Redis, Depends(get_redis)]):
    pipeline = redis.pipeline()
    pipeline.lrange(f"user-{id}", 0, -1)
    pipeline.delete(f"user-{id}")
    result = await pipeline.execute()
    keys = result[0]
    pipeline = redis.pipeline()
    for key in keys:
        pipeline.hgetall(key)
    messages = await pipeline.execute()
    return [from_db_to_json(msg) for msg in messages]


@app.get("/user/{id}/flash/serialized", response_class=ORJSONResponse)
async def get_messages_serialized(id: int, redis: Annotated[Redis, Depends(get_redis)]):
    pipeline = redis.pipeline()
    pipeline.lrange(f"user-{id}-serialized", 0, -1)
    pipeline.delete(f"user-{id}-serialized")
    result = await pipeline.execute()
    return ORJSONResponse(result[0])
