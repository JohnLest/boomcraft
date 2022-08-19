import socket
import selectors
import logging
import types
from typing import Dict
import threading

from apis.boomcraftApi import BoomcraftApi
from app.gameController import GameController
from tool import *

class Server:
    def __init__(self, host="0.0.0.0", port=8080):
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.dico_connect = {}
        self.s_n_connect = {}
        self.boomcraft_api = BoomcraftApi()
        self.game_controller = GameController(self)

    # region communication
    def __connection(self):
        # AF_INET == ipv4
        # SOCK_STREAM == TCP
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((self.host, self.port))
        lsock.listen()
        self.logger.debug(f"listening on {self.host}:{self.port}")
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

    def __accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        self.logger.info(f"accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def __service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                self.logger.info(f'receive data : {recv_data}')
                data.outb += recv_data
                new_message = threading.Thread(target=self.__analyse_msg, args=(deserialize(data.outb), key, ), daemon=True)
                new_message.start()
            else:
                self.logger.info(f'client closing connection to{data.addr}', )
                self.sel.unregister(sock)
                sock.close()
            data.outb = b''

    def connect(self):
        self.__connection()
        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.__accept_wrapper(key.fileobj)
                else:
                    self.__service_connection(key, mask)

    def write(self, key, message):
        sock = key.fileobj
        msg_bytes = serialize(message)
        while len(msg_bytes) != 0:
            sent = sock.send(msg_bytes)
            msg_bytes = msg_bytes[sent:]

    def send_all(self, msg):
        for key in self.dico_connect.values():
            self.write(key, msg)

    # endregion

    # region Analyse Message
    def __analyse_msg(self, msg: Dict, key_socket):
        key = first_or_default(msg)
        if key is None:
            return
        body: Dict = msg.get(key, None)
        if msg is None:
            return
        id_user = get_key(self.dico_connect, key_socket)
        self.logger.info(f"Receive new message - key : {key} - id user : {id_user}")
        if key == 1:
            body.update({"connection_type": "login"})
            id_user = self.game_controller.new_player(key_socket, **body)
            if id_user is not None:
                self.dico_connect.update({id_user: key_socket})
        elif key == 2:
            body.update({"connection_type": "new"})
            id_user = self.game_controller.new_player(key_socket, **body)
            if id_user is not None:
                self.dico_connect.update({id_user: key_socket})
        elif key == 3:
            self.game_controller.update_resources(id_user, body)
        elif key == 4:
            self.game_controller.add_player_game(body.get("id_user"))
        elif key == 5:
            self.game_controller.init_player_in_gui(id_user, body)
        elif key == 6:
            id_worker = first_or_default(body)
            self.game_controller.move_worker(id_worker, body.get(id_worker))
        elif key == 7:
            self.game_controller.new_forum(body)
        elif key == 100:
            pass
            # self.s_n_connect.update({body.get("uuid"): key_socket})
        elif key == 101:
            pass
            """
            _uuid = body.pop("uuid")
            body.update({"connection_type": "facebook"})
            user: PlayerInfoModel = self.__new_player(self.s_n_connect.get(_uuid), **body)
            msg = user.dict()
            msg.pop("key_socket")
            self.write(user.key_socket, {1: msg})
            # self.write(self.dico_connect.get(body.get("id")), {1: msg})
            """
        elif key == 201:
            pass
            # uri = "http://dataservice.accuweather.com/currentconditions/v1/"
            # weather_api = OtherApi(uri)
            # weather = weather_api.get_request("27581?apikey=NM6IwoED21vbDTI6Fc7gosRt9A5rqNTu")
            # self.write(key_socket, {201: weather})
        elif key == 202:
            pass
            """
            uri2 = "https://nominis.cef.fr/json"
            saint_api = OtherApi(uri2)
            saint = saint_api.get_request("saintdujour.php")
            light_saint = saint.get("response").get("saintdujour")
            light_saint.pop("contenu")
            light_saint.pop("lien")
            light_saint.update(saint.get("response").get("query"))

            print(saint)
            test = serialize(saint)
            val = len(test)
            self.write(key_socket, {202: saint})
            """

    # endregion
