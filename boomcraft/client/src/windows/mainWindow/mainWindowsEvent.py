import time
import pygame


from src.windows.mainWindow.mainWindow import MainWindow


class MainWindowEvent:
    def __init__(self, main_win: MainWindow):
        self.main_win = main_win
        self.__event()

    def __event(self):
        # btn = self.main_win.btnAPI
        while True:
            self.main_win.group.update()
            self.main_win.group.draw(self.main_win.gbGame.surface)
            self.main_win.update_gb_banner_resources()
            self.main_win.gbGame.show_groupbox(self.main_win.window)
            self.__handle_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"click on {event.pos[0]} - {event.pos[1]}")
                    if event.button == 1:
                        self.__left_click(event)
                    elif event.button == 3:
                        self.__right_click()

            pygame.display.update()

    def __left_click(self, event):
        for key, worker in self.main_win.all_worker.items():
            if worker.absolute_rect.collidepoint(pygame.mouse.get_pos()):
                if worker.id_owner != self.main_win.user.user.id_user: return
                self.main_win.set_target(worker.id, worker.x, worker.y)
                self.main_win.destroy_forum_button()
                self.main_win.set_worker_buttons()
                return
        for key, forum in self.main_win.all_forum.items():
            if forum.absolute_rect.collidepoint(pygame.mouse.get_pos()):
                if forum.id_owner != self.main_win.user.user.id_user: return
                self.main_win.set_target(forum.id, forum.x, forum.y)
                self.main_win.destroy_worker_button()
                self.main_win.set_forum_button()
                return
        if self.main_win.target is not None and self.main_win.gbGame.data_rect.collidepoint(pygame.mouse.get_pos()):
            if self.main_win.all_worker.get(self.main_win.target.id_to_target) is not None:
                pos_x = event.pos[0] - self.main_win.gbGame.data_rect.x
                pos_y = event.pos[1] - self.main_win.gbGame.data_rect.y
                if pos_x > self.main_win.gbGame.data_rect.width - 17:
                    pos_x = self.main_win.gbGame.data_rect.width - 17
                if pos_y > self.main_win.gbGame.data_rect.height - 33:
                    pos_y = self.main_win.gbGame.data_rect.height - 33
                self.main_win.connection.write({6: {self.main_win.target.id_to_target: (pos_x, pos_y)}})
            return
        if self.main_win.target is not None and self.main_win.gbAction.data_rect.collidepoint(pygame.mouse.get_pos()):
            for id, worker_button in self.main_win.all_worker_buttons.items():
                if worker_button.absolute_rect.collidepoint(pygame.mouse.get_pos()):
                    self.main_win.connection.write({7: self.main_win.target.id_to_target})
                    return
            for id, forum_button in self.main_win.all_forum_buttons.items():
                if forum_button.absolute_rect.collidepoint(pygame.mouse.get_pos()):
                    self.main_win.connection.write({8: self.main_win.target.id_to_target})
                    return
        """
        if btn.btn_rect.collidepoint(pygame.mouse.get_pos()):
            self.main_win.menu_sprite.enlarge()
            self.main_win.menu_sprite.menu_strip_item.draw(self.main_win.window)
            self.__menu_strip_on_click()
        """

    def __right_click(self):
        if self.main_win.target is not None:
            self.main_win.destroy_target()
            self.main_win.destroy_worker_button()
            self.main_win.destroy_forum_button()

    def __menu_strip_on_click(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_win.menu_sprite.menu_strip_item_dict.get("twitch").rect.collidepoint(
                            pygame.mouse.get_pos()):
                        print("Un")
                    elif self.main_win.menu_sprite.menu_strip_item_dict.get("fcb").rect.collidepoint(
                            pygame.mouse.get_pos()):
                        print("Deux")
                    elif self.main_win.menu_sprite.menu_strip_item_dict.get("discord").rect.collidepoint(
                            pygame.mouse.get_pos()):
                        print("Long")
                    else:
                        self.main_win.menu_sprite.tighten()
                        self.main_win.gbGame.show_groupbox(self.main_win.window)
                        return

    def __handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            print("up")
            time.sleep(0.5)
        if pressed[pygame.K_s]:
            print("down")
        if pressed[pygame.K_a]:
            print("left")
        if pressed[pygame.K_d]:
            print("right")
