import socket
import time

from tool import deserialize, serialize

HOST = "127.0.0.1"
PORT = 8080


def main():
    print(f"Hello client")
    obj = {1: "hi2", 2: "test"}
    msg = serialize(obj)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg)
        while True:
            data = s.recv(1024)
            print('Received', deserialize(data))


if __name__ == "__main__":
    main()
