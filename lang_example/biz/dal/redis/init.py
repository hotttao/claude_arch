# Redis 连接初始化

import redis

def init_redis_client(config):
    """初始化Redis客户端"""
    client = redis.Redis(
        host=config.host,
        port=config.port,
        db=config.db,
        decode_responses=True
    )
    return client