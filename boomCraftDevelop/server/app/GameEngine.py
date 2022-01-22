from typing import Dict
from app import GameServer
from app import PlayerInGame
from app.Party import Party


class GameEngine():
    """ 
    the GameEngine that will be the brain of the game 
    """

    def __init__(self, width: int, height: int) :

        self.__width = width
        """ The play board width """

        self.__height = height
        """ The play board  height"""

        self.__party_nb = 0
        """ The next number available to assign to a new party """

        self.__game_server : GameServer = None
        """ Core Class of the GameServer where we receive and send all the messages from and to the clients  """

        self.__parties : Dict[int,Party] = None 
        """ The existing parties  """


    def add_party(self) :
        """ prepare the next party """
        new_party : Party = Party('0',self, self.__party_nb);
        new_party.create_party();
        self.__parties[self.__party_nb] = new_party;
    

    def update_gui(self, party_nb : int) :
        """ Ask to send board to all players of a party
            :param party_nb the party number 
        """
        self.__game_server.update(party_nb);

    def update_gui(self, ip_addr : str) :
        """ Ask to send -basic- board to one specific player arriving on the game window
        :param ip_addr the client ip address
        """
        self.__game_server.update(ip_addr);


    def move_mobile(self, player : PlayerInGame, id_mobile_entity : int) :
        """ Ask to send -basic- board to one specific player arriving on the game window
        :param player the player in game
        :param id_mobile_entity the id of the mobile entity of the player that has to move to another position
        """
     
 
    
    

    def send_base_board(self, ip_addr : str) :
        """ Send the basic board
        :param ip_addr the client ip address
        """
        print("Send base board for player waiting for a new game");
        self.update_gui(ip_addr);

    
     
     
    def everyone_is_ready(self, party_nb : int) :
        """ Start game when everyone noticed "ready to play"
        :param party_nb the number of the party 
        """
        #nothing to do for the moment 12112022
         


    

    def treat_event(self, to_be_defined : any, player : PlayerInGame) :
        """ Treat an event for a player
        :param to_be_defined PARAM TO BE DEFINED 
        :param player from which comes the event 
        """
    


    def update_score(self, player : PlayerInGame , value : int, last_survivor : bool) :
        """ 
        Update the score of a player
        :param player the player in game structure
        :param value to add to the score of the player
        :param lastSurvivor boolean indicating the fact that the player is the last survivor or not
        """

    
    def add_ready(self, party_nb : int, place: int, state : bool) :
        """ 
        Put the ready state of a client based on its partyNumber,idPlayer and state
        :param party_nb the party number
        :param place the number of the player in the game
        :param state the state of the player  
        """






    ################################################################
    #  Getters and Setters
    ################################################################

    def set__width(self, width : int):
        self.__width = width

    def get__width(self) :
        return self.__width

    def set__height(self, height : int):
        self.__height = height

    def get__height(self) :
        return self.__height

    def set__party_nb(self, party_nb : int):
        self.__party_nb = party_nb

    def get__party_nb(self) :
        return self.__party_nb

    def set__game_server(self, game_server : GameServer):
        self.__game_server = game_server

    def get__game_server(self) :
        return self.__game_server

    def set__parties(self, parties : Dict[int,Party]):
        self.__parties = parties

    def get__parties(self) :
        return self.__parties
   