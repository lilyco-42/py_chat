import socket


def main() -> None:
    # 创建 socket
    s = socket.socket(socket.AF_INET, socket.SocketKind.SOCK_STREAM)
    PORT: int = 3000
    s.bind(("127.0.0.1", PORT))
    print("Hello from py-chat!")
    s.listen(5)

    while True:
        c, addr = s.accept()
        print(f"{c}.|{addr}|")
        while True:
            data = c.recv(1024)
            print(data.decode("utf-8"))
            c.send(data.upper())
        s.close()


if __name__ == "__main__":
    main()
