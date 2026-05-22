# HTTPX异步HTTP客户端

## 基本请求
```python
import httpx

async def fetch():
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.example.com/data')
        return resp.json()
```

## 超时与重试
```python
client = httpx.AsyncClient(
    timeout=httpx.Timeout(10.0, connect=5.0),
    limits=httpx.Limits(max_connections=100),
)
```

## 流式响应
```python
async with client.stream('GET', url) as resp:
    async for chunk in resp.aiter_bytes():
        process(chunk)
```

## HTTP/2支持
```python
client = httpx.AsyncClient(http2=True)
```

---
*编号: R058-#0526 | 更新时间: 2026-05-22T14:45:15Z | 仓库: dev-utils*
