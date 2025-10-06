# FastAPI 服务启动入口

import uvicorn
from fastapi import FastAPI
from config import get_config
from biz.router.register import register_routers
from biz.dal.mysql.init import init_mysql_pool

def create_app():
    """创建 FastAPI 应用"""
    app = FastAPI(
        title="Langchain Example API",
        description="基于 Langchain 和 FastAPI 的示例项目",
        version="1.0.0"
    )

    # 注册路由
    register_routers(app)

    return app

def main():
    """主函数"""
    # 加载配置
    config = get_config()

    # 初始化数据库连接池
    init_mysql_pool(config.database.mysql)

    # 创建应用
    app = create_app()

    # 启动服务
    uvicorn.run(
        app,
        host=config.server.host,
        port=config.server.port,
        debug=config.server.debug
    )

if __name__ == "__main__":
    main()