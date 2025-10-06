# 认证处理器

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from biz.handler.auth_models import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from biz.service.auth_service import AuthService
from biz.dal.mysql.init import get_db
from biz.dal.model.user import User

# 创建路由器
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """用户登录"""
    user = AuthService.authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = AuthService.create_access_token_for_user(user)
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        username=user.username
    )

@router.post("/register", response_model=RegisterResponse)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """用户注册"""
    user = AuthService.create_user(db, request.username, request.email, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名或邮箱已存在",
        )

    return RegisterResponse(
        user_id=user.id,
        username=user.username,
        email=user.email
    )