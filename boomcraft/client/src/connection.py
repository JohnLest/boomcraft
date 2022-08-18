import selectors
import socket
import types
import logging
from tool import *
import time


class Connection:
    def __init__(self, host, port):
        self.logger = logging.getLogger(__name__)
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
        tst = message.get(4)
        if tst is not None:
            time.sleep(0.1)
            print("Send Message")
        sock = self.key.fileobj
        message_bytes = serialize(message)
        if message_bytes == b'':
            self.logger.warning(f"Tentative to send an empty message")
            return
        if tst is not None:
            print("Message serialized")
        while len(message_bytes) != 0:
            sent = sock.send(message_bytes)
            message_bytes = message_bytes[sent:]

        if tst is not None:
            print("End Send Message")
