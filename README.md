# 头条新闻后端 (Toutiao Backend)

## 核心特性

- **现代化技术栈**：基于 FastAPI 框架，支持全异步 (AsyncIO) 处理，提供极致的并发性能。
- **规范化工程结构**：采用标准的 `src` 布局，将业务代码与配置文件、文档、前端代码彻底隔离，避免循环导入，提升可维护性。
- **完善的业务模块**：
    - **新闻模块**：支持新闻分类、列表分页、详情获取及相关新闻推荐。
    - **收藏模块**：支持用户新闻的收藏与取消收藏，具备防重复插入机制。
    - **历史记录**：支持浏览历史的记录（防重复刷新）、分页查询、单条删除及一键清空。
- **高性能缓存体系**：全面接入 Redis，为新闻分类、列表、详情及相关新闻提供“Cache Aside（旁路缓存）”策略，大幅降低数据库查询压力。
- **现代包管理**：使用 `uv` 进行极速的依赖管理与环境隔离。
- **前后端分离**：项目内置前端工程 (`wzx-news`)，支持一体化开发。

## ️ 技术栈

- **Web 框架**: FastAPI, Uvicorn
- **数据库**: SQLAlchemy (Async), MySQL/PostgreSQL
- **缓存**: Redis (redis.asyncio)
- **数据校验**: Pydantic V2
- **包管理工具**: uv

## 项目结构

```text
xwzx-news/
├── src/                    # 核心 Python 业务源码
│   └── toutiao_backend/
│       ├── config/         # 配置模块 (DB, Redis等)
│       ├── cache/          # 缓存业务逻辑 (Key生成, 读写策略)
│       ├── crud/           # 数据库操作与缓存优先查询逻辑
│       ├── models/         # SQLAlchemy ORM 模型
│       ├── routers/        # API 路由层
│       ├── schemas/        # Pydantic 数据校验与响应模型
│       ├── utils/          # 通用工具类
│       └── main.py         # 应用启动入口
├── wzx-news/               # 前端代码 (Vue/React等)
├── docs/                   # 项目物料 (API文档, 数据库SQL, 设计说明)
├── tests/                  # 接口测试文件
├── pyproject.toml          # 项目核心配置与依赖声明
├── uv.lock                 # 依赖版本锁定文件
└── README.md               # 项目说明文档
```

## 快速开始

1. **环境要求**
    - Python >= 3.10
    - Redis 服务已启动
    - MySQL/PostgreSQL 数据库已配置
2. **安装依赖**
   使用 `uv` 极速安装项目依赖：

```bash
uv sync
```

3. **配置环境变量**
   请在 `config/` 目录下配置好你的数据库连接信息和 Redis 连接信息。
4. **启动服务**

```bash
uv run python src/toutiao_backend/main.py
```

服务启动后，可通过浏览器访问自动生成的交互式 API 文档：
`http://127.0.0.1:8000/docs`

## ️ 接口概览

- 新闻接口 (/news)：获取分类、列表、详情、相关新闻
- 收藏接口 (/favorite)：添加收藏、获取收藏列表、取消收藏
- 历史接口 (/history)：添加历史、获取历史列表、删除单条、清空历史

## ️ 贡献

欢迎提交 Issue 或 Pull Request 来完善本项目！