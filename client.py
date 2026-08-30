import socket
from ast import While

if __name__ == "__main__":
    s = socket.socket()

    port = 3000  # 设置端口号

    s.connect(("127.0.0.1", port))

    while True:
        msg = "Welcome"
        s.send(msg.encode("utf-8"))
        data = s.recv(1024)
        print(f"{data.decode('utf-8')}")
