from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # 1. 处理 GET 请求
    def do_GET(self):
        # 设置响应状态码
        self.send_response(200)
        # 设置响应头
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()

        # 定义返回内容
        response = {
            "status": "success",
            "message": "这是来自原生 Python HTTP 服务的响应",
            "path": self.path,
        }

        # 写入响应体
        self.wfile.write(json.dumps(response).encode("utf-8"))

    # 2. 处理 POST 请求
    def do_POST(self):
        # 获取请求体的长度
        content_length = int(self.headers["Content-Length"])
        # 读取原始字节流
        post_data = self.rfile.read(content_length)

        # 尝试解析 JSON
        try:
            data = json.loads(post_data.decode("utf-8"))
            print(f"收到数据: {data}")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"message": "数据已收到", "received": data}
            self.wfile.write(json.dumps(response).encode("utf-8"))

        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(str(e).encode())


# 3. 启动服务器
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"服务启动在 http://localhost:{port} ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()