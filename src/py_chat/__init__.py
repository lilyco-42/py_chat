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
        data = c.recv(1024)
        c.send(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain; charset=utf-8\r\n"
            b"Content-Length: 13\r\n"
            b"Connection: close\r\n"
            b"\r\n"
            b"Hello, World!"
        )
        c.close()


if __name__ == "__main__":
    main()
