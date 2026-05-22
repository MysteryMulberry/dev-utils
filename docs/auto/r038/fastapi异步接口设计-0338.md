# FastAPI异步接口设计

## 基本异步路由
```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/api/data")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.example.com/data")
        return resp.json()
```

## 依赖注入
```python
from fastapi import Depends

async def get_db():
    db = await database.connect()
    try:
        yield db
    finally:
        await db.disconnect()

@app.get("/users")
async def get_users(db = Depends(get_db)):
    return await db.fetch_all("SELECT * FROM users")
```

## 中间件
```python
@app.middleware("http")
async def add_process_time(request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start)
    return response
```

---
*编号: R038-#0338 | 更新时间: 2026-05-22T07:46:04Z | 仓库: dev-utils*
