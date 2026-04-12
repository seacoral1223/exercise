import urllib.request
import json


def test_get():
    print("--- 正在测试 GET 请求 ---")
    url = "http://localhost:8001"

    try:
        # 1. 发起请求并获取响应
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            headers = response.info()
            body = response.read().decode("utf-8")

            print(f"状态码: {status_code}")
            print(f"响应内容: {body}")
    except Exception as e:
        print(f"请求失败: {e}")


def test_post():
    print("\n--- 正在测试 POST 请求 ---")
    url = "http://localhost:8001"

    # 2. 准备要发送的数据（JSON 格式）
    data = {"model": "cat_dog_recognition", "action": "predict", "id": 123}

    # 将字典转为字节流
    json_bytes = json.dumps(data).encode("utf-8")

    # 3. 构造 Request 对象（需要手动指定 Content-Type）
    req = urllib.request.Request(url, data=json_bytes, method="POST")
    req.add_header("Content-Type", "application/json; charset=utf-8")

    try:
        with urllib.request.urlopen(req) as response:
            print(f"状态码: {response.getcode()}")
            print(f"响应内容: {response.read().decode('utf-8')}")
    except Exception as e:
        print(f"请求失败: {e}")


if __name__ == "__main__":
    # 请确保你的服务端已经启动并在 8000 端口监听
    test_get()
    test_post()