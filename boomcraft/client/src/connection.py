import selectors
import socket
import types
from tool import *


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.mask = 0
        self.key = None

    def connection(self):
        server_addr = (self.host, self.port)
        print(f'starting connection to {server_addr}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(outb=b'')
        self.sel.register(sock, events, data=data)

    def write(self, message):
        sock = self.key.fileobj
        message_bytes = serialize(message)
        while len(message_bytes) != 0:
            sent = sock.send(message_bytes)
            message_bytes = message_bytes[sent:]
