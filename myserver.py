from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #设置头的回复
        self.send_response(200)
        #设置同样的内容类型
        self.send_header('Content-Type', 'application/json; charset=utf-8')  
        #关闭头
        self.end_headers()

        res = ("你好吗？")

        self.wfile.write(json.dumps(res).encode("utf-8"))
        # self.wfile.write(res.encode("utf-8"))

    def do_POST(self):
        content_text_size = int(self.headers['Content-Length'])
        data = self.rfile.read(content_text_size)

        try:
            tran_data = json.loads(data.decode("utf-8"))
            print("接收到的数据：", tran_data)

            self.send_response(200)

            self.send_header('Content-Type', 'application/json; charset=utf-8')

            self.end_headers()
            res = "我已收到数据"
            self.wfile.write(json.dumps(res).encode("utf-8"))
            # self.wfile.write(res.encode("utf-8"))
        except Exception as e:
            print("数据解析失败：", e)


http = HTTPServer(server_address=('', 8001), RequestHandlerClass=MyRequestHandler).serve_forever()

