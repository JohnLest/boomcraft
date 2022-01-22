import time
import threading
from app.GameEngine import GameEngine
from app.GameServer import GameServer

MAX_WIDTH_SIZE = 840
MAX_HEIGTH_SIZE = 540

def main():
    
    ge : GameEngine = GameEngine(MAX_WIDTH_SIZE,MAX_HEIGTH_SIZE)


    gs : GameServer = GameServer(ge , MAX_WIDTH_SIZE, MAX_HEIGTH_SIZE, 2, 55555)

