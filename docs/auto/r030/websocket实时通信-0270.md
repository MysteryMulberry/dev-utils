# WebSocket实时通信

## FastAPI WebSocket
```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        await ws.send_text(f"Echo: {data}")
```

## 广播模式
```python
class ConnectionManager:
    def __init__(self):
        self.connections: list[WebSocket] = []

    async def broadcast(self, message: str):
        for conn in self.connections:
            await conn.send_text(message)

manager = ConnectionManager()
```

## 前端连接
```javascript
const ws = new WebSocket('ws://localhost:8000/ws');
ws.onmessage = (event) => console.log(event.data);
ws.send('Hello');
```

---
*编号: R030-#0270 | 更新时间: 2026-05-22T07:39:03Z | 仓库: dev-utils*
