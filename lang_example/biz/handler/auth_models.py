# 认证请求和响应模型

from pydantic import BaseModel, Field
from typing import Optional

class LoginRequest(BaseModel):
    """登录请求模型"""
    username: str = Field(..., min_length=1, max_length=50, description="用户名")
    password: str = Field(..., min_length=6, max_length=100, description="密码")

class LoginResponse(BaseModel):
    """登录响应模型"""
    access_token: str = Field(..., description="访问令牌")
    token_type: str = Field("bearer", description="令牌类型")
    user_id: int = Field(..., description="用户ID")
    username: str = Field(..., description="用户名")

class RegisterRequest(BaseModel):
    """注册请求模型"""
    username: str = Field(..., min_length=1, max_length=50, description="用户名")
    email: str = Field(..., min_length=5, max_length=100, description="邮箱地址")
    password: str = Field(..., min_length=6, max_length=100, description="密码")

class RegisterResponse(BaseModel):
    """注册响应模型"""
    user_id: int = Field(..., description="用户ID")
    username: str = Field(..., description="用户名")
    email: str = Field(..., description="邮箱地址")