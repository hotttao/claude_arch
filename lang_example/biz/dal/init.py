# 数据库连接初始化

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from biz.dal.model.user import User  # 导入用户模型以确保表被创建

# 数据库基类
Base = declarative_base()

def init_mysql_connection(config):
    """初始化MySQL连接"""
    # 实现MySQL连接逻辑
    pass

def init_redis_connection(config):
    """初始化Redis连接"""
    # 实现Redis连接逻辑
    pass