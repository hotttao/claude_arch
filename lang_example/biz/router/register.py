# 路由注册入口

from fastapi import FastAPI
from biz.handler import auth_router

def register_routers(app: FastAPI):
    """注册所有路由"""
    # 在这里注册各个模块的路由
    app.include_router(auth_router)