# MySQL 连接池初始化

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from biz.dal.init import Base

# 全局变量存储引擎和会话
engine = None
SessionLocal = None

def init_mysql_pool(config):
    """初始化MySQL连接池"""
    global engine, SessionLocal

    engine = create_engine(
        f"mysql+pymysql://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}",
        poolclass=QueuePool,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=config.debug
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # 创建所有表
    Base.metadata.create_all(bind=engine)

    return engine, SessionLocal

def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()