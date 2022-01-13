import json
import socket
import selectors
import threading
import types
from typing import List, Dict
from boomcraftApi import BoomcraftApi

from tool import *

HOST = "127.0.0.1"
PORT = 8080
sel = selectors.DefaultSelector()
dico_connect = {}
boomcraft_api = BoomcraftApi()


def connection():
    # AF_INET == ipv4
    # SOCK_STREAM == TCP
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    print('listening on', (HOST, PORT))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
        analyse_msg(deserialize(data.outb), key)


def write(sock, message: List[bytes]):
    while len(message) != 0:
        sent = sock.send(message)
        message = message[sent:]


def send_all(msg):
    for key in dico_connect.values():
        write(key.fileobj, serialize(msg))


def analyse_msg(msg: Dict, key_socket):
    key = first_or_default(msg)
    if key is None:
        return
    body = msg.get(key, None)
    if msg is None:
        return
    if key == 1:
        mail = body.get("mail")
        password = body.get("password")
        user = boomcraft_api.connect(mail, password)
        print(f"Le pseudo est : {user.get('pseudo')}")
        dico_connect[user.get('id_user')] = key_socket
        send_all({1: user})
    if key == 2:
        user = boomcraft_api.post_new_user(json.dumps(body))
        print(f"Le pseudo est : {user.get('pseudo')}")
        dico_connect[user.get('id_user')] = key_socket
        send_all({1: user})



def main():
    print(f"Hello server")
    connection()
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)


if __name__ == "__main__":
    main()