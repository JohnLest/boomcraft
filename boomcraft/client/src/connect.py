import socket
from tool import deserialize, serialize

HOST = "127.0.0.1"
PORT = 8080


def connect(_msg):
    print(f"Hello client")
    msg = serialize(_msg)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg)
        while True:
            data = s.recv(1024)
            print('Received', deserialize(data))


