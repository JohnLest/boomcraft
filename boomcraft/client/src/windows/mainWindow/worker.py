import pygame
import threading
import time

CHARACTER_UP = "../resources/mainWindows/up/0.png"
CHARACTER_DOWN = "../resources/mainWindows/down/0.png"
CHARACTER_LEFT = "../resources/mainWindows/left/0.png"
CHARACTER_RIGHT = "../resources/mainWindows/right/0.png"

class Worker(pygame.sprite.Sprite):
    def __init__(self, connection, x: int = 0, y: int = 0, width: int = 16, height: int = 32):
        super().__init__()
        self.coord: list = [x, y]
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.destination: list[int] = []
        self.road_to_destination = [[]]
        self.current_step: list[int] = []
        self.connection = connection
        self.farm_resource_thread = threading.Thread()
        self.stop_farm = True

        self.img_up = pygame.image.load(CHARACTER_UP).convert_alpha()
        self.img_down = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.img_left = pygame.image.load(CHARACTER_LEFT).convert_alpha()
        self.img_right = pygame.image.load(CHARACTER_RIGHT).convert_alpha()

        self.image = self.img_down  # pygame.Surface((16, 32))
        self.rect = self.image.get_rect()
        # self.image.blit(self.img_down, (0, 0), (self.x, self.y, self.width, self.height))
        # self.rect = self.image.get_rect()

    def __thread_farm(self, resource):
        count = 0
        while True:
            if resource == "trees":
                time.sleep(1)
                if self.stop_farm: return
                if count % 5 == 4:
                    self.connection.write({7: {"food": 10}})
                self.connection.write({7: {"wood": 10}})
            elif resource == "stone":
                time.sleep(1)
                if self.stop_farm: return
                self.connection.write({7: {"stone": 10}})
            elif resource == "ore":
                time.sleep(2)
                if self.stop_farm: return
                if count % 5 == 4:
                    self.connection.write({7: {"gold": 5}})
                self.connection.write({7: {"iron": 10}})
            if self.stop_farm: return
            count += 1

    def update(self):
        self.rect.topleft = [self.x, self.y]

    def farm_resources(self, resource, is_farming):
        if is_farming:
            self.stop_farm = False
            self.farm_resource_thread = threading.Thread(target=self.__thread_farm, args=(resource,), daemon=True)
            self.farm_resource_thread.start()
            print("start")
        elif not is_farming:
            self.stop_farm = True
            self.farm_resource_thread.join()
        print("test")
