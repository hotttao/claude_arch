# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Langchain and FastAPI-based AI Agent microservice system designed to provide an extensible and maintainable intelligent agent platform.

## Architecture

The project follows a strict layered architecture:

1. **Protocol Offloading Layer** (`infra`): Handles transport protocols and infrastructure-related code
2. **Business Layer** (`biz`): Pure business logic code with three-tier architecture:
   - `core` layer (`internal`): Core business logic, implementing independent basic business units
   - `service` layer (`biz/service`): Business process orchestration, can call multiple cores
   - `handler` layer (`biz/handler`): Connection layer between protocol and business, responsible for input validation and output presentation
3. **Shared Code Principles**: Each layer's shared logic must be placed in that layer's unique `shared` directory

Directory structure:
```
lang_example/
├── agent/              # Langchain Agent implementation
├── api/                # API interface definitions (protobuf IDL)
├── biz/                # Business layer
├── config/             # Configuration files
├── infra/              # Infrastructure layer
├── internal/           # Core business layer
├── middleware/         # Global middleware
├── ui/                 # Frontend interface
└── server.py           # Service entry point
```

## Common Development Commands

### Installation and Setup
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python server.py
```

Configuration is managed using Hydra with environment-specific configs:
- `dev.yaml`: Development environment
- `test.yaml`: Testing environment
- `prod.yaml`: Production environment

### Dependencies
- FastAPI >= 0.100.0
- Uvicorn >= 0.20.0
- Langchain >= 0.1.0
- SQLAlchemy >= 2.0.0
- PyMySQL >= 1.0.0
- Redis >= 4.0.0
- Hydra-core >= 1.3.0
- Pydantic >= 2.0.0

## Key Implementation Details

1. **Configuration Management**: Uses Hydra with Pydantic schemas for type-safe configuration
2. **Database Access**: Uses SQLAlchemy ORM for MySQL and Redis for caching
3. **Routing**: Routes are registered in `biz/router/register.py`
4. **Layered Architecture**: Strict separation between infrastructure, business logic, and protocol layers
5. **Agent Implementation**: Langchain agents are implemented in the `agent/` directory with tools, nodes, and graph structures

## Development Guidelines

1. Follow the three-tier architecture pattern in the business layer
2. Place shared logic in each layer's `shared` directory only
3. Maintain strict layering - lower layers must never call upper layers
4. Use Hydra for all configuration management
5. Implement database models in `biz/dal/model/` with corresponding data access in `biz/dal/mysql/`