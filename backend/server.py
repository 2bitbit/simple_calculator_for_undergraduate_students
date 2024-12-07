from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import threading
from utils.paths import BASE_PATH


class Server:
    def __init__(self):
        self.app = FastAPI()
        self.app.mount(
            "/", StaticFiles(directory=BASE_PATH, html=True), name="static"
        )  # 将目录挂载为静态文件目录
        self.port = 8000

    def start(self):
        threading.Thread(
            target=lambda: uvicorn.run(app=self.app, host="127.0.0.1", port=self.port),
            daemon=True,
        ).start()