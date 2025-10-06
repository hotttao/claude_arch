# Agent 相关的数据类型定义

from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class AgentInput(BaseModel):
    """Agent 输入数据模型"""
    query: str
    context: Optional[Dict[str, Any]] = None
    history: Optional[List[Dict[str, str]]] = None

class AgentOutput(BaseModel):
    """Agent 输出数据模型"""
    response: str
    intermediate_steps: Optional[List[Any]] = None
    metadata: Optional[Dict[str, Any]] = None