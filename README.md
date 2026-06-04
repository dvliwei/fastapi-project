# FastAPI Project

一个基于 FastAPI 的项目示例，当前包含基础应用配置、用户接口路由和 Pydantic 数据模型。

## 项目结构

```text
fastapi-project/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── goods.py
│   │       └── user.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   ├── schemas.py
│   │   └── usermodel.py
│   ├── utils/
│   │   └── common.py
│   └── main.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## 环境要求

- Python 3.12+
- FastAPI
- Uvicorn
- pydantic-settings

## 安装依赖

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 环境变量

复制示例配置：

```bash
cp .env.example .env
```

当前支持的配置项：

```env
APP_NAME=FastAPI Project
PORT=8000
RELOAD=True
```

说明：

- `APP_NAME`：应用名称
- `PORT`：服务端口
- `RELOAD`：是否开启自动重载

## 启动项目

推荐使用：

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

也可以直接运行：

```bash
python -m app.main
```

启动后访问：

- 接口文档：http://127.0.0.1:8000/docs
- ReDoc 文档：http://127.0.0.1:8000/redoc

## 当前接口

### 获取用户列表

```http
GET /users/list
```

示例请求：

```bash
curl http://127.0.0.1:8000/users/list
```

示例响应：

```json
[
  {
    "user_id": 1,
    "username": "alice",
    "email": "alice@example.com",
    "password": null
  },
  {
    "user_id": 2,
    "username": "bob",
    "email": "bob@example.com",
    "password": null
  }
]
```

## Git 仓库

远程仓库：

```text
git@github.com:dvliwei/fastapi-project.git
```

## 注意事项

- `.env`、`venv/`、`.idea/`、`__pycache__/` 等本地文件不会提交到 Git。
- 项目入口为 `app.main:app`。
- 根目录不再使用独立的 `main.py`，避免和 `app/main.py` 混淆。
