import pygame
import pyscroll.data
import pytmx.util_pygame

from widget import *
from window import Window


class MainWindow(Window):
    """ Class for main window """
    def __init__(self):
        self.main_win = Window.__init__(self, (1200, 900), "Boomcraft")
        self.__gb_menu_button()
        self.__gb_resource_banner()
        self.__gb_game()
        self.__gb_action()
        self.__menu_strip_api()

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
        self.wood = ImageAndText("../resources/wood.png",
                                 "wood : 2632",
                                 position_midleft=(self.resource_position_x * 0, self.gbResourceBanner.data_rect.midleft[1])
                                )
        self.food = ImageAndText("../resources/food.png",
                                 "food : 2632",
                                 position_midleft=(self.resource_position_x * 1, self.gbResourceBanner.data_rect.midleft[1])
                                )
        self.iron = ImageAndText("../resources/iron.png",
                                 "iron : 2632",
                                 position_midleft=(self.resource_position_x * 2, self.gbResourceBanner.data_rect.midleft[1])
                                )
        self.stone = ImageAndText("../resources/stone.png",
                                 "stone : 2632",
                                 position_midleft=(self.resource_position_x * 3, self.gbResourceBanner.data_rect.midleft[1])
                                )
        self.gold = ImageAndText("../resources/gold.png",
                                 "gold : 2632",
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

        tmx_data = pytmx.util_pygame.load_pygame("../resources/map/BoomCraft_map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.gbGame.surface.get_size())
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        group.draw(self.gbGame.surface)

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
