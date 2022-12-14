import time
import pygame
import pyscroll.data
import pytmx.util_pygame
import selectors
import threading
import logging

from src.models.playerInfoModel import PlayerInfoModel
from src.windows.mainWindow.gameObject.forum import Forum
from tool import *
from src.windows.mainWindow.gameObject.worker import Worker
from src.windows.menuWindow import MenuWindow
from src.windows.mainWindow.window import Window
from src.windows.mainWindow.widget import *
from src.windows.mainWindow.gameObject.target import Target
from src.windows.mainWindow.gameObject.workerButton import WorkerButton
from src.windows.mainWindow.gameObject.forumButton import ForumButton
from src.windows.mainWindow.gameObject.boss import Boss
from src.windows.mainWindow.gameObject.name import Name


class MainWindow(Window):
    """ Class for main window """
    def __init__(self, connection):
        self.logger = logging.getLogger(__name__)
        self.connection = connection
        self.disconnection = False
        self.connection.connection()
        thread = threading.Thread(target=self.__thread_read, daemon=True)
        thread.start()

        self.user = None
        self.id_game = None
        self.saint = None
        self.meteo = None
        self.flappy_resources = {}
        self.path_resources = "../resources/mainWindows"
        self.dict_resources = {}
        self.all_worker = {}
        self.all_forum = {}
        self.boss = None
        self.target = None
        self.button_worker = pygame.sprite.Group()
        self.button_forum = pygame.sprite.Group()
        self.all_worker_buttons = {}
        self.all_forum_buttons = {}
        self.__set_game()
        self.end_game = False
        if not self.menuWin.new_game:
            self.disconnection = True
            thread.join()
            return

        self.main_win = Window.__init__(self, (1200, 900), f"Boomcraft - {self.user.user.pseudo}")
        self.__gb_menu_button()
        self.__gb_resource_banner()
        self.__gb_game()
        self.__gb_action()
        self.__menu_strip_api()

    # region Set Game

    def __set_game(self):
        time.sleep(0.5)
        self.menuWin = MenuWindow(self.connection, self)
        if self.menuWin.new_game:
            self.connection.write({4: {"id_user": self.user.user.id_user}})
            while True:
                if self.id_game is not None:
                    break
            self.get_game_resources()
        if len(self.menuWin.window.children) != 0:
            self.menuWin.window.destroy()

    def __gb_menu_button(self):
        """ GroupBox for Menu Button """
        self.gbMenuButton = GroupBox(
            (0, 0),
            (self.winXPercent * 10, self.winYPercent * 5),
            (0, 0, 0)
        )
        self.btnAPI = Button(self.window, "API", rect=self.gbMenuButton.data_rect)
        return self

    def __gb_resource_banner(self):
        """ GroupBox for banner resources """
        self.gbResourceBanner = GroupBox(
            (self.gbMenuButton.data_rect.topright[0], self.gbMenuButton.data_rect.topright[1]),
            (self.winXPercent * 90, self.winYPercent * 5),
            (0, 0, 0)
        )
        self.resource_position_x = self.gbResourceBanner.data_rect.width / 5
        self.wood = ImageAndText(f"{self.path_resources}/wood.png",
                                 f"wood : {self.dict_resources.get('wood')}",
                                 position_midleft=(self.resource_position_x * 0, self.gbResourceBanner.data_rect.midleft[1])
                                 )
        self.food = ImageAndText(f"{self.path_resources}/food.png",
                                 f"food : {self.dict_resources.get('food')}",
                                 position_midleft=(self.resource_position_x * 1, self.gbResourceBanner.data_rect.midleft[1])
                                 )
        self.iron = ImageAndText(f"{self.path_resources}/iron.png",
                                 f"iron : {self.dict_resources.get('iron')}",
                                 position_midleft=(self.resource_position_x * 2, self.gbResourceBanner.data_rect.midleft[1])
                                 )
        self.stone = ImageAndText(f"{self.path_resources}/stone.png",
                                  f"stone : {self.dict_resources.get('stone')}",
                                  position_midleft=(self.resource_position_x * 3, self.gbResourceBanner.data_rect.midleft[1])
                                  )
        self.gold = ImageAndText(f"{self.path_resources}/gold.png",
                                 f"gold : {self.dict_resources.get('gold')}",
                                 position_midleft=(self.resource_position_x * 4, self.gbResourceBanner.data_rect.midleft[1])
                                 )
        self.update_gb_banner_resources()
        return self

    def __gb_game(self):
        """ GroupBox for the play board """
        self.gbGame = GroupBox(
            (self.gbMenuButton.data_rect.bottomleft[0], self.gbMenuButton.data_rect.bottomleft[1]),
            (1120, self.winYPercent * 80),
            (255, 0, 0)
        )
        self.gbGame.data_rect.midtop = (self.winX / 2, self.gbGame.data_rect.midtop[1])

        tmx_data = pytmx.util_pygame.load_pygame(f"{self.path_resources}/map/BoomCraft_map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.gbGame.surface.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        self.connection.write({5: self.id_game})
        # self.group.update()

        self.group.draw(self.gbGame.surface)
        self.gbGame.show_groupbox(self.window)
        return self

    def __gb_action(self):
        """ GroupBox for the action in game """
        self.gbAction = GroupBox(
            (self.gbGame.data_rect.bottomleft[0], self.gbGame.data_rect.bottomleft[1]),
            (self.winX, self.winYPercent * 15),
            (0, 0, 0)
        )
        self.gbAction.show_groupbox(self.window)
        return self

    def __menu_strip_api(self):
        self.menu_stripe_dict = {"twitch": "Twitch", "fcb": "Facebook", "discord": "Discord"}
        self.menu_sprite = MenuStrip(self.btnAPI.btn_rect, self.menu_stripe_dict)

    def get_game_resources(self):
        game_resources = self.user.game_resources
        for resource in game_resources:
            self.dict_resources.update({resource.resource: resource.quantity})

    def update_gb_banner_resources(self):
        self.get_game_resources()
        self.wood.update_text(f"wood : {self.dict_resources.get('wood')}")
        self.food.update_text(f"food : {self.dict_resources.get('food')}")
        self.stone.update_text(f"stone : {self.dict_resources.get('stone')}")
        self.iron.update_text(f"iron : {self.dict_resources.get('iron')}")
        self.gold.update_text(f"gold : {self.dict_resources.get('gold')}")
        self.gbResourceBanner.surface.fill((0, 0, 0))
        self.wood.show_image_and_text(self.gbResourceBanner.surface)
        self.food.show_image_and_text(self.gbResourceBanner.surface)
        self.iron.show_image_and_text(self.gbResourceBanner.surface)
        self.stone.show_image_and_text(self.gbResourceBanner.surface)
        self.gold.show_image_and_text(self.gbResourceBanner.surface)
        self.gbResourceBanner.show_groupbox(self.window)

    def set_target(self, id_to_target, x, y):
        if self.target is not None: self.destroy_target()
        self.target = Target(id_to_target, x, y)
        self.group.add(self.target)
        self.group.update()

    def destroy_target(self):
        self.group.remove(self.target)
        del self.target
        self.target = None
        self.group.update()

    def set_worker_buttons(self):
        if self.all_worker_buttons != {}: self.destroy_worker_button()
        new_button = WorkerButton(50, self.gbAction.data_rect.midleft[1] - self.gbAction.data_rect.topleft[1])
        self.all_worker_buttons.update({new_button.id: new_button})
        self.button_worker.add(new_button)
        self.button_worker.update()
        self.button_worker.draw(self.gbAction.surface)
        self.gbAction.show_groupbox(self.window)

    def destroy_worker_button(self):
        for id, button in self.all_worker_buttons.items():
            self.button_worker.remove(button)
            del button
        self.all_worker_buttons.clear()
        self.button_worker.update()
        self.gbAction.surface.fill((0, 0, 0))
        self.button_worker.draw(self.gbAction.surface)
        self.gbAction.show_groupbox(self.window)

    def set_forum_button(self):
        if self.all_forum_buttons != {}: self.destroy_forum_button()
        new_button = ForumButton(50, self.gbAction.data_rect.midleft[1] - self.gbAction.data_rect.topleft[1])
        self.all_forum_buttons.update({new_button.id: new_button})
        self.button_forum.add(new_button)
        self.button_forum.update()
        self.button_forum.draw(self.gbAction.surface)
        self.gbAction.show_groupbox(self.window)

    def destroy_forum_button(self):
        for id, button in self.all_forum_buttons.items():
            self.button_forum.remove(button)
            del button
        self.all_forum_buttons.clear()
        self.button_forum.update()
        self.gbAction.surface.fill((0, 0, 0))
        self.button_forum.draw(self.gbAction.surface)
        self.gbAction.show_groupbox(self.window)



    # endregion

    # region Comunicate
    def __thread_read(self):
        while True:
            events = self.connection.sel.select(timeout=None)
            if self.disconnection:
                break
            if first_or_default(events) is not None:
                self.connection.key, self.connection.mask = first_or_default(events)
                self.__read()

    def __read(self):
        sock = self.connection.key.fileobj
        data = self.connection.key.data
        if self.connection.mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print('closing connection')
                self.connection.sel.unregister(sock)
                sock.close()
            self.__analyse_msg(deserialize(data.outb))
            data.outb = b''

    def __analyse_msg(self, msg: dict):
        if msg is None:
            self.logger.warning(f"Empty message ")
            return
        key = first_or_default(msg)
        if key is None:
            return
        body: dict = msg.get(key, None)
        if msg is None:
            return
        if key == 1:
            if body is not None:
                self.user = PlayerInfoModel(**body)
            else:
                self.user = "bad request"
        elif key == 2:
            self.user = PlayerInfoModel(**body)
        elif key == 3:
            self.id_game = body.get("id_game")
        elif key == 4:
            pass

        elif key == 101:
            body = first_or_default(body)
            w_text = body.get("WeatherText")
            temp = body.get("Temperature").get("Metric").get("Value")
            unit = body.get("Temperature").get("Metric").get("Unit")

            self.meteo = f"Brussels meteo : {w_text} - {temp}.{unit}"
        elif key == 102:
            day = body.get("response").get("saintdujour").get("jour")
            mounth = body.get("response").get("saintdujour").get("mois")
            years = body.get("response").get("saintdujour").get("annee")
            name = body.get("response").get("saintdujour").get("nom")
            self.saint = f"{day}/{mounth}/{years} : {name}"
        elif key == 103:
            self.flappy_resources = body

        elif key == 500:
            _all_worker: dict = body[0]
            _all_forum: dict = body[1]
            _boss: dict = body[2]
            for id_worker, worker_data in _all_worker.items():
                _worker: Worker = self.all_worker.get(id_worker)
                if _worker is None:
                    new_worker = Worker(id_worker, worker_data.get("owner"), x=worker_data.get("x"), y=worker_data.get("y"))
                    self.group.add(new_worker)
                    self.all_worker.update({new_worker.id: new_worker})
                    continue
                _worker.x = worker_data.get("x")
                _worker.y = worker_data.get("y")
                _worker.life = worker_data.get("life")
                if self.target is not None and self.target.id_to_target == _worker.id:
                    self.target.x = _worker.x
                    self.target.y = _worker.y
                if _worker.life == 0:
                    self.all_worker.pop(_worker.id)
                    self.group.remove(_worker)
                    del _worker

            for id_forum, forum_data in _all_forum.items():
                _forum: Forum = self.all_forum.get(id_forum)
                if _forum is None:
                    new_forum = Forum(id_forum, forum_data.get("owner"), x=forum_data.get("x"), y=forum_data.get("y"))
                    self.group.add(new_forum)
                    self.all_forum.update({new_forum.id: new_forum})
                    continue
                _forum.life = forum_data.get("life")
                if _forum.life == 0:
                    self.all_forum.pop(_forum.id)
                    self.group.remove(_forum)
                    del _forum

            if self.boss is None:
                self.boss = Boss(id_boss=_boss.get("id_boss"),
                                 name=_boss.get("name"),
                                 x=_boss.get("x"),
                                 y=_boss.get("y"),
                                 life=_boss.get("life"))
                self.group.add(self.boss)

                new_name = Name(self.boss.name, self.boss.x, self.boss.y)
                self.boss.name_items = new_name
                self.group.add(new_name)
            else:
                self.boss.life = _boss.get("life")
            if self.boss.life == 0:
                self.boss.x = 0
                self.boss.y = 0
                self.boss.height = 0
                self.boss.width = 0
                self.group.remove(self.boss.name_items)
                self.group.remove(self.boss)

            self.group.update()
            self.group.draw(self.gbGame.surface)
            self.gbGame.show_groupbox(self.window)
            pygame.display.update()
        elif key == 666:
            if body == "win":
                pass
            elif body == "loose":
                pass
            self.end_game = True
    # endregion
