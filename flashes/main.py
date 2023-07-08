import orjson as json
from fastapi import FastAPI
from flashes.redis import init_redis_pool
from shortuuid import uuid
from flashes import fake

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("startando o repo")
    app.state.redis = await init_redis_pool()

@app.on_event("shutdown")
async def shutdown_event():
    print("fechando as conn tudo")
    await app.state.redis.close()

@app.get("/create_all/hash")
async def create_all_hash():
    flashes_content: list[dict] = fake.get_all_flashes()
    keys = []
    for content in flashes_content:
        _key = uuid()
        keys.append(_key)
        await app.state.redis.hset(_key, mapping=content)
        await app.state.redis.rpush("user-1", _key)
    return keys

@app.get("/create_all/serialized")
async def create_all_serialized():
    flashes_content: list[dict] = fake.get_all_flashes(serialized=True)
    
    pipeline = app.state.redis.pipeline()
    for content in flashes_content:
        pipeline.rpush("user-1-serialized", json.dumps(content))

    await pipeline.execute()
    return {"key": "user-1-serialized"}

def from_db_to_json(_from: dict) -> dict:
    return {
        "msg": _from["msg"],
        "key": _from["key"],
        "values": json.loads(_from["values"])
    }

def from_db_to_json_serialized(_from: str) -> dict:
    return json.loads(_from)

@app.get("/user/{id}/flash")
async def get_messages(id: int):
    pipeline = app.state.redis.pipeline()
    pipeline.lrange(f"user-{id}", 0, -1)
    pipeline.delete(f"user-{id}")
    result = await pipeline.execute()
    keys = result[0]
    pipeline = app.state.redis.pipeline()
    for key in keys:
        pipeline.hgetall(key)
    messages = await pipeline.execute()
    return [from_db_to_json(msg) for msg in messages]


@app.get("/user/{id}/flash/serialized")
async def get_messages_serialized(id: int):
    pipeline = app.state.redis.pipeline()
    pipeline.lrange(f"user-{id}-serialized", 0, -1)
    pipeline.delete(f"user-{id}-serialized")
    result = await pipeline.execute()
    return [from_db_to_json_serialized(msg) for msg in result[0]]
