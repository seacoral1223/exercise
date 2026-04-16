import socket
sever_addr = "127.0.0.1"
sever_port = 8002
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((sever_addr,sever_port))
while True:
    input_str = input("[+]")
    if input_str == "quit":
        break
    client.send(input_str.encode("utf-8"))
    data = client.recv(2048)
    print(data.decode("utf-8"))

client.close()