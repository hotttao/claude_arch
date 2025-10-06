# Agent 节点定义

from typing import Dict, Any
from langchain_core.runnables import Runnable
from .type import AgentInput, AgentOutput

class BaseNode:
    """Agent 节点基类"""

    def __init__(self, name: str):
        self.name = name

    def execute(self, input_data: AgentInput) -> AgentOutput:
        """执行节点逻辑"""
        raise NotImplementedError("子类必须实现 execute 方法")

class ToolNode(BaseNode):
    """工具调用节点"""

    def __init__(self, name: str, tool: Runnable):
        super().__init__(name)
        self.tool = tool

    def execute(self, input_data: AgentInput) -> AgentOutput:
        # 实现工具调用逻辑
        pass

class ReasoningNode(BaseNode):
    """推理节点"""

    def __init__(self, name: str, llm: Runnable):
        super().__init__(name)
        self.llm = llm

    def execute(self, input_data: AgentInput) -> AgentOutput:
        # 实现推理逻辑
        pass