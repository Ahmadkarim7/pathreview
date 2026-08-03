"""Shared Redis client for dependency injection."""

from collections.abc import AsyncGenerator

import redis.asyncio as redis

from core.config import settings

_redis_pool: redis.ConnectionPool = redis.ConnectionPool.from_url(
    settings.redis_url, decode_responses=True
)


async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    """Dependency for FastAPI that yields a Redis client."""
    client = redis.Redis(connection_pool=_redis_pool)
    try:
        yield client
    finally:
        await client.close()
