# Langchain Example Project

基于 Langchain 和 FastAPI 构建的 AI Agent 微服务系统。

## 项目结构

```
lang_example/
├── agent/              # Langchain Agent 实现
├── api/                # API 接口定义
├── biz/                # 业务层
├── config/             # 配置文件
├── infra/              # 基础设施层
├── internal/           # 核心业务层
├── middleware/         # 全局中间件
├── ui/                 # 前端界面
├── arch_design.md      # 架构设计文档
├── micro_design.md     # 微服务设计文档
└── server.py           # 服务启动入口
```

## 技术栈

- FastAPI
- Langchain
- MySQL
- Redis
- SQLAlchemy
- Hydra (配置管理)

## 快速开始

1. 安装依赖
2. 配置环境变量
3. 启动服务

## 配置

使用 Hydra 进行配置管理，支持多环境配置。

## 架构说明

详细架构设计请参考 [arch_design.md](arch_design.md)
微服务设计请参考 [micro_design.md](micro_design.md)