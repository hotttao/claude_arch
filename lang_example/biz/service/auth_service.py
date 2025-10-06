# 用户认证服务

from sqlalchemy.orm import Session
from biz.dal.mysql.user_dao import UserDAO
from biz.shared.password_utils import verify_password, get_password_hash
from biz.shared.jwt_utils import create_access_token
from datetime import timedelta
from typing import Optional
from config import get_config

# 获取配置
config = get_config()

class AuthService:
    """用户认证服务"""

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[dict]:
        """验证用户凭据"""
        user = UserDAO.get_user_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_user(db: Session, username: str, email: str, password: str) -> Optional[dict]:
        """创建新用户"""
        # 检查用户名是否已存在
        existing_user = UserDAO.get_user_by_username(db, username)
        if existing_user:
            return None

        # 检查邮箱是否已存在
        existing_email = UserDAO.get_user_by_email(db, email)
        if existing_email:
            return None

        # 创建新用户
        hashed_password = get_password_hash(password)
        user = UserDAO.create_user(db, username, email, hashed_password)
        return user

    @staticmethod
    def create_access_token_for_user(user: dict) -> str:
        """为用户创建访问令牌"""
        access_token_expires = timedelta(minutes=config.security.access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": user.username, "user_id": user.id},
            expires_delta=access_token_expires
        )
        return access_token