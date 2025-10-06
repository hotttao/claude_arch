# JWT令牌处理工具

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from config import get_config

# 获取配置
config = get_config()

# JWT配置
SECRET_KEY = config.security.secret_key
ALGORITHM = config.security.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.security.access_token_expire_minutes

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建访问令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str) -> Optional[dict]:
    """验证访问令牌"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None