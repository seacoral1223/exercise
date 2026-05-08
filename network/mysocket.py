import socket
import os
import subprocess
import threading

addr="127.0.0.1"
port=8002


def handle_connect(conn:socket):
    while True:
        data = conn.recv(1024)
        data_str = data.decode("utf-8")
        os.system(data_str)

        if data_str == "quit":
            break
        conn.send("服务器已收到数据".encode("utf-8"))
#3. 返回消息

if __name__ == "__main__":
    #1.创建一个socket对象
#tcp协议：socket.AF_INET,socket.SOCK_STREAM
#udp协议：socket.AF_INET,socket.SOCK_DGRAM

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((addr,port))
    server.listen(10)
    #2.利用创建的socket对象连接服务器
    conn,address = server.accept()

    handle_connect(conn)

    #4. 关闭连接
    server.close()