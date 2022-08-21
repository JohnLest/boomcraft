import selectors
import socket
import time
import types
import threading
from typing import Dict
from tool import *


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.mask = 0

    def __connection(self):
        server_addr = (self.host, self.port)
        print(f'starting connection to server : {server_addr}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(outb=b'')
        self.sel.register(sock, events, data=data)

    def __thread_read(self):
        while True:
            events = self.sel.select(timeout=None)
            if first_or_default(events) is not None:
                self.key, self.mask = first_or_default(events)
                self.read()

    def service(self):
        self.__connection()
        thread = threading.Thread(target=self.__thread_read)
        thread.start()
        time.sleep(0.5)

    def read(self):
        sock = self.key.fileobj
        data = self.key.data
        if self.mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print('closing connection to', data.addr)
                self.sel.unregister(sock)
                sock.close()
            self.analyse_msg(deserialize(data.outb))
            data.outb = b''

    def write(self, message):
        sock = self.key.fileobj
        message_bytes = serialize(message)
        while len(message_bytes) != 0:
            sent = sock.send(message_bytes)
            message_bytes = message_bytes[sent:]

    def analyse_msg(self, msg: Dict):
        key = first_or_default(msg)
        if key is None:
            return
        body = msg.get(key, None)
        if msg is None:
            return
        if key == 101:
            print(f"Connexion réussie {body}")



