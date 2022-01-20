
from typing import Dict
from app.PlayerInGame import PlayerInGame
from app.game_structure.PlayArea import PlayArea
from app.GameEngine import GameEngine


class Party():


    def __init__(self, id_uniq: str = '0', ge: GameEngine = None, party_nb : int = -1) :


        self.__id_uniq: str = id_uniq
        """ The id of the party """
        self.__ge = ge
        """ The gameEngine (brain of the game) """
        self.__party_nb = party_nb
        """ The number of the party """
        self.__players : Dict[int, PlayerInGame] = None
        """ The players of the game """
        self.__players_ips : Dict[int,str]= None 
        """ The ipAddresses of the players of the game """
        self.__players_ready : Dict[int,bool]= None 
        """ The ready state of the players """
        self.__game_over : bool = False 
        """ The state of the party """
        self.__play_area : PlayArea = None 
        """ The play board  """


    ################################################################
    #  Methods
    ################################################################

    def create_party(self) :
        """ 
        Create the party
        The playboard, the entities and their representations on the board
        """

        # -->  WORK IN PROGRESS


    ################################################################
    #  Getters and Setters
    ################################################################

    def set__id_uniq(self, id_uniq : str):
        self.__id_uniq = id_uniq

    def get__id_uniq(self) :
        return self.__id_uniq



    def set__ge(self, ge : GameEngine):
        self.__ge = ge
    def get__ge(self) :
        return self.__ge    



    def set__party_nb(self, party_nb : str):
        self.__party_nb = party_nb

    def get__party_nb(self) :
        return self.__party_nb



    def set__players(self, players: Dict[int,PlayerInGame]):
        self.__players = players

    def get__players(self) :
        return self.__players



    def set__players_ips(self, players_ips: Dict[int,str]):
        self.__players_ips = players_ips

    def get__players_ips(self) :
        return self.__players_ips



    def set__players_ready(self, players_ready : Dict[int,bool]):
        self.__players_ready = players_ready

    def get__players_ready(self) :
        return self.__players_ready



    def set__game_over(self, game_over : bool):
        self.__game_over = game_over

    def get__game_over(self) :
        return self.__game_over



    def set__play_area(self, play_area : PlayArea):
        self.__play_area = play_area

    def get__play_area(self) :
        return self.__play_area