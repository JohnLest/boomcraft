import time
import pygame
import pyscroll.data
import pytmx.util_pygame
import selectors
import threading

from src.models.playerInfoModel import PlayerInfoModel
from src.windows.mainWindow.gameObject.forum import Forum
from tool import *
from src.windows.mainWindow.gameObject.worker import Worker
from src.windows.menuWindow import MenuWindow
from src.windows.mainWindow.window import Window
from src.windows.mainWindow.widget import *


class MainWindow(Window):
    """ Class for main window """
    def __init__(self, connection):
        self.connection = connection
        self.disconnection = False
        self.connection.connection()
        thread = threading.Thread(target=self.__thread_read, daemon=True)
        thread.start()

        self.user = None
        self.id_game = None
        self.saint = None
        self.meteo = None
        self.path_resources = "../resources/mainWindows"
        self.hitbox_trees = []
        self.hitbox_stone = []
        self.hitbox_ore = []
        self.dict_resources = {}
        self.__set_game()
        if not self.menuWin.new_game:
            self.disconnection = True
            thread.join()
            return

        self.main_win = Window.__init__(self, (1200, 900), "Boomcraft")
        self.__gb_menu_button()
        self.__gb_resource_banner()
        self.__gb_game()
        self.__gb_action()
        self.__menu_strip_api()
        self.connection.write({5: {"worker_coord": (self.worker.x, self.worker.y),
                                   "forum_coord": (self.forum.x, self.forum.y)}
                               })


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
        for hit_res in tmx_data.objects:
            if hit_res.type == "trees":
                self.hitbox_trees.append(pygame.Rect(hit_res.x, hit_res.y, hit_res.width, hit_res.height))
            elif hit_res.type == "stone":
                self.hitbox_stone.append(pygame.Rect(hit_res.x, hit_res.y, hit_res.width, hit_res.height))
            elif hit_res.type == "ore":
                self.hitbox_ore.append(pygame.Rect(hit_res.x, hit_res.y, hit_res.width, hit_res.height))

        self.worker = Worker(self.connection, 100, 150)
        self.forum = Forum(600, 600)
        self.group.add(self.worker)
        self.group.add(self.forum)
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
        self.connection.write({201: {"weather": True}})
        time.sleep(0.1)
        self.connection.write({202: {"saint": True}})
        while True:
            if self.meteo is not None and self.saint is not None:
                break
        font = pygame.font.SysFont("Arial", 18)
        text_render = font.render(f"{self.saint} - {self.meteo}", True, (255, 255, 255))
        rect_text = text_render.get_rect()
        rect_text.x = rect_text.x + 5
        pygame.draw.rect(self.gbAction.surface, (0, 0, 0), rect_text, 1)
        self.gbAction.surface.blit(text_render, (250, 50))
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
        key = first_or_default(msg)
        if key is None:
            return
        body: dict = msg.get(key, None)
        if msg is None:
            return
        if key == 1:
            self.user = PlayerInfoModel(**body)
        elif key == 2:
            self.user = PlayerInfoModel(**body)
        elif key == 3:
            self.id_game = body.get("id_game")

        elif key == 201:
            body = first_or_default(body)
            w_text = body.get("WeatherText")
            temp = body.get("Temperature").get("Metric").get("Value")
            unit = body.get("Temperature").get("Metric").get("Unit")

            self.meteo = f"Brussels meteo : {w_text} - {temp}.{unit}"
        elif key == 202:
            day = body.get("response").get("saintdujour").get("jour")
            mounth = body.get("response").get("saintdujour").get("mois")
            years = body.get("response").get("saintdujour").get("annee")
            name = body.get("response").get("saintdujour").get("nom")
            self.saint = f"{day}/{mounth}/{years} : {name}"

        elif key == 500:
            self.worker.x = body.get("new_coord")[0]
            self.worker.y = body.get("new_coord")[1]
            self.group.update()
            self.group.draw(self.gbGame.surface)
            self.gbGame.show_groupbox(self.window)
            pygame.display.update()
        elif key == 501:
            self.group.remove(self.forum)
            self.group.update()
            self.group.draw(self.gbGame.surface)
            self.gbGame.show_groupbox(self.window)
            pygame.display.update()
            print("forum detruit")
    # endregion