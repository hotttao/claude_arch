# 项目架构设计文档

## 项目概述

本项目是一个基于 Langchain 和 FastAPI 构建的 AI Agent 微服务系统，旨在提供一个可扩展、可维护的智能代理平台。

## 技术栈

- **框架**: FastAPI + Langchain
- **数据库**: MySQL + Redis
- **ORM**: SQLAlchemy
- **配置管理**: Hydra
- **依赖管理**: uv

## 架构设计原则

### 1. 协议卸载
- **infra 层**: 处理传输协议、微服务治理等基础设施相关代码
- **业务层**: 纯业务逻辑代码
- **严格分层**: 下层代码绝不调用上层代码

### 2. 三层架构
业务层采用严格的三层架构：
- **core 层** (`internal`): 最底层核心业务逻辑，实现独立的业务基本单元
- **service 层** (`biz/service`): 中间层，负责业务流程编排，可调用多个 core
- **handler 层** (`biz/handler`): 顶层，协议层与业务的连接层，负责输入验证与输出展示

### 3. 共享代码规范
- 每层的共享逻辑必须放在该层唯一的 `shared` 目录中
- 禁止创建通用的 utils 文件
- 只能使用 `shared` 文件存放公共逻辑

## 目录结构

```
lang_example/
├── agent/              # Langchain Agent 实现目录
│   ├── tools/          # 自定义工具
│   ├── nodes/          # Agent 节点定义
│   ├── graphs/         # Agent 图结构定义
│   ├── __init__.py
│   ├── type.py         # Agent 数据类型定义
│   ├── node.py         # 节点基类和实现
│   └── graph.py        # 图结构定义
├── api/                # API 接口定义（protobuf IDL）
├── biz/                # 业务层
│   ├── dal/            # 数据访问层
│   │   ├── model/      # ORM 模型定义
│   │   ├── mysql/      # MySQL 连接和操作
│   │   ├── redis/      # Redis 连接和操作
│   │   ├── __init__.py
│   │   └── init.py     # 数据库初始化
│   ├── handler/        # 请求处理器
│   ├── router/         # 路由定义和注册
│   ├── service/        # 业务服务层
│   ├── shared/         # 业务层共享逻辑
│   └── __init__.py
├── config/             # 配置文件
│   ├── env/            # 环境特定配置
│   ├── __init__.py
│   ├── const.py        # 常量定义
│   ├── schema.py       # 配置模式定义
│   └── conf.yaml       # 默认配置
├── infra/              # 基础设施层
│   ├── shared/         # 基础设施共享逻辑
│   └── __init__.py
├── internal/           # 核心业务层
│   ├── shared/         # 核心层共享逻辑
│   └── __init__.py
├── middleware/         # 全局中间件
│   └── __init__.py
├── ui/                 # 前端界面
├── arch_design.md      # 架构设计文档
├── micro_design.md     # 微服务设计文档
└── server.py           # 服务启动入口
```

## 实现流程

1. 根据业务需求进行服务拆分
2. 设计数据库和接口
3. 使用 Protobuf 定义 IDL 接口
4. 按照三层架构实现业务逻辑
5. 记录微服务设计到 `micro_design.md`

## 配置管理

使用 Hydra 进行配置管理，支持多环境配置：
- `dev.yaml`: 开发环境
- `test.yaml`: 测试环境
- `prod.yaml`: 生产环境

## 数据库设计

- **MySQL**: 主要数据存储
- **Redis**: 缓存和会话存储
- 使用 SQLAlchemy ORM 进行数据访问

## 微服务设计

微服务设计细节将记录在 `micro_design.md` 文件中，包括：
- 服务拆分原则
- 每个服务的职责
- 服务间通信方式