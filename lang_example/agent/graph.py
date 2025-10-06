# Agent 图定义

from typing import Dict, List, Any
from .node import BaseNode
from .type import AgentInput, AgentOutput

class AgentGraph:
    """Agent 图结构"""

    def __init__(self):
        self.nodes: Dict[str, BaseNode] = {}
        self.edges: Dict[str, List[str]] = {}

    def add_node(self, node: BaseNode):
        """添加节点"""
        self.nodes[node.name] = node

    def add_edge(self, from_node: str, to_node: str):
        """添加边"""
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)

    def execute(self, input_data: AgentInput) -> AgentOutput:
        """执行图"""
        # 实现图执行逻辑
        pass