import threading
import time


from typing import Dict, List
from GameEngine import GameEngine

from Worker import WORKER

class Party(threading.Thread):
    
    def __init__(self, thread_id : int, game_engine : GameEngine, workers : Dict[int, WORKER]) :
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.game_engine : GameEngine = game_engine
        self.teams : List[WORKER] = None
        self.workers : Dict[int, WORKER] = workers
        self.game_over = False

    def run(self):

        while (self.game_over != True):
            print ("Starting ", self.thread_id)
            
            for worker in self.workers : 
                if(self.workers[worker].destination !=[]) :
                    self.game_engine.move_mobile(self.workers[worker])
            time.sleep(1)

            print ("Exiting ", self.thread_id)

''' 
class Team(): 
'''
