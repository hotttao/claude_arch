# 配置模块初始化文件

from .schema import ConfigSchema, ServerConfig, MySQLConfig, RedisConfig, LoggingConfig

# 全局配置对象
CONFIG = None

def load_config():
    """加载配置文件"""
    global CONFIG
    # 这里会使用 hydra-core 来加载配置
    # 暂时使用默认配置
    CONFIG = ConfigSchema()
    return CONFIG

def get_config(force=False):
    """获取配置对象"""
    global CONFIG
    if CONFIG is None or force:
        return load_config()
    return CONFIG