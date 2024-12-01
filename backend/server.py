from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading  # 在新线程中运行服务器


class Server:
    def __init__(self):
        port = 8000
        self.server = HTTPServer(("", port), SimpleHTTPRequestHandler)

    def start(self):
        threading.Thread(target=self.server.serve_forever, daemon=True).start()