import socket
import selectors
import logging
import time
import types
from typing import Dict
import threading
from apis.boomcraftApi import BoomcraftApi
from gameObjects.forum import Forum
from gameObjects.otherApi import OtherApi
from playerRepo import PlayerRepo
from gameEngine import GameEngine
from models.playerInfoModel import PlayerInfoModel
from tool import *
from gameObjects.worker import Worker


class Server:
    def __init__(self, host="0.0.0.0", port=8080):
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.dico_connect = {}
        self.s_n_connect = {}
        self.boomcraft_api = BoomcraftApi()
        self.game_engine = GameEngine(self)

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
                data.outb += recv_data
                new_message = threading.Thread(target=self.__analyse_msg, args=(deserialize(data.outb), key, ), daemon=True)
                new_message.start()
                # self.__analyse_msg(deserialize(data.outb), key)
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
        if key == 1:
            mail = body.get("mail")
            password = body.get("password")
            user: PlayerInfoModel = self.__new_player(key_socket, connection_type="login", mail=mail, password=password)
            msg = user.dict()
            msg.pop("key_socket")
            self.write(key_socket, {1: msg})
        elif key == 2:
            body.update({"connection_type": "new"})
            user: PlayerInfoModel = self.__new_player(key_socket, **body)
            msg = user.dict()
            msg.pop("key_socket")
            self.write(key_socket, {1: msg})
        elif key == 3:
            up_player = self.game_engine.player_repo.update_resources(id_user, body)
            msg = up_player.dict()
            msg.pop("key_socket")
            self.write(key_socket, {2: msg})
        elif key == 4:
            id_game = self.game_engine.add_player_in_game(self.game_engine.player_repo.lst_player.get(body.get("id_user")))
            self.write(key_socket, {3: {"id_game": id_game}})
        elif key == 5:
            new_worker = None
            id_game = body
            if self.game_engine.game_lst.get(id_game)[0].model_player.user.id_user == id_user:
                new_worker = self.game_engine.player_repo.create_worker(id_user, 100, 100)
            elif self.game_engine.game_lst.get(id_game)[1].model_player.user.id_user == id_user:
                new_worker = self.game_engine.player_repo.create_worker(id_user, 300, 300)
            if new_worker is not None:
                self.game_engine.update_gui(id_game)
            # TODO to remove :
            self.forum = Forum(600, 600)
        elif key == 6:
            for worker in self.game_engine.player_repo.lst_player.get(id_user).workers:
                if worker.id_worker == first_or_default(body):
                    worker.destination = [body.get(worker.id_worker)[0], body.get(worker.id_worker)[1]]
                    self.game_engine.update_road_to_destination(worker, self.forum)
                    break
        elif key == 7:
            farm_player = self.game_engine.player_repo.farm_resources(get_key(self.dico_connect, key_socket), body)
            msg = farm_player.dict()
            msg.pop("key_socket")
            self.write(key_socket, {2: msg})

        elif key == 100:
            self.s_n_connect.update({body.get("uuid"): key_socket})
        elif key == 101:
            _uuid = body.pop("uuid")
            body.update({"connection_type": "facebook"})
            user: PlayerInfoModel = self.__new_player(self.s_n_connect.get(_uuid), **body)
            msg = user.dict()
            msg.pop("key_socket")
            self.write(user.key_socket, {1: msg})
            # self.write(self.dico_connect.get(body.get("id")), {1: msg})
        elif key == 201:
            pass
            # uri = "http://dataservice.accuweather.com/currentconditions/v1/"
            # weather_api = OtherApi(uri)
            # weather = weather_api.get_request("27581?apikey=NM6IwoED21vbDTI6Fc7gosRt9A5rqNTu")
            # self.write(key_socket, {201: weather})
        elif key == 202:
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

    def __new_player(self, key_socket, **data):
        user: PlayerInfoModel = self.game_engine.player_repo.new_player(key_socket, **data)
        self.dico_connect[user.user.id_user] = key_socket
        return user

    def __add_game(self, id_player):
        return self.game_engine.add_player_in_game(self.game_engine.player_repo.lst_player.get(id_player))

    # endregion
