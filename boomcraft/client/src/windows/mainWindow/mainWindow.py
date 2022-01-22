import pygame
import pyscroll.data
import pytmx.util_pygame

from src.windows.mainWindow.worker import Worker
from src.windows.menuWindow import MenuWindow
from src.windows.mainWindow.window import Window
from src.windows.mainWindow.widget import *

import os


class MainWindow(Window):
    """ Class for main window """
    def __init__(self, connection):
        self.connection = connection
        self.path_resources = "../resources/mainWindows"
        self.__set_game()
        self.__get_game_resources()

        self.main_win = Window.__init__(self, (1200, 900), "Boomcraft")
        self.__gb_menu_button()
        self.__gb_resource_banner()
        self.__gb_game()
        self.__gb_action()
        self.__menu_strip_api()



    def __set_game(self):
        self.connection.service()
        self.menuWin = MenuWindow(self.connection)
        if self.menuWin.new_game:
            print("Start Game")
            print(self.connection.user)
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
        self.wood.show_image_and_text(self.gbResourceBanner.surface)
        self.food.show_image_and_text(self.gbResourceBanner.surface)
        self.iron.show_image_and_text(self.gbResourceBanner.surface)
        self.stone.show_image_and_text(self.gbResourceBanner.surface)
        self.gold.show_image_and_text(self.gbResourceBanner.surface)
        self.gbResourceBanner.show_groupbox(self.window)
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
        self.worker = Worker(100, 150)
        self.group.add(self.worker)
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
        return self

    def __menu_strip_api(self):
        self.menu_stripe_dict = {"twitch": "Twitch", "fcb": "Facebook", "discord": "Discord"}
        self.menu_sprite = MenuStrip(self.btnAPI.btn_rect, self.menu_stripe_dict)

    def __get_game_resources(self):
        game_resources = self.connection.user.game_resources
        self.dict_resources = {}
        for resource in game_resources:
            self.dict_resources.update({resource.resource: resource.quantity})
