"""
Phase 0: 两块屏第一次说话
电脑跑这个服务，手机连同一个 WiFi 打开浏览器，点按钮，电脑屏幕上弹气泡。

跑法：
    pip install fastapi uvicorn
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json

app = FastAPI(title="两屏互联 Phase 0")

# 所有连着的客户端（手机 / 电脑上的浏览器都算）
clients: list[WebSocket] = []


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print(f"[连接] 当前在线客户端: {len(clients)}")
    try:
        while True:
            raw = await websocket.receive_text()
            msg = json.loads(raw)
            text = msg.get("text", "")
            print(f"[收到] {text}")
            # 广播给所有连着的端（包括手机自己，也包括电脑屏幕）
            for c in clients:
                await c.send_text(json.dumps({"text": text}))
    except WebSocketDisconnect:
        clients.remove(websocket)
        print(f"[断开] 当前在线客户端: {len(clients)}")


# 静态页面：手机和电脑都打开这个
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")
