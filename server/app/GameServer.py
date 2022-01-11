from typing import ByteString, Dict
from app.game_entity.Character import Character
from app.GameEngine import GameEngine
from app.game_structure.PlayArea import PlayArea


class GameServer():
    """
    Core Class of the GameServer
    
    Here we receive and send all the messages from and to the clients
    """
    def __init__(self, game_engine : GameEngine, width: int, height: int, number_of_player_in_a_game : int = 2, number_of_port : int = 55555):

        self.__width=width
        """ The play board width """

        self.__height=height
        """ The play board  height"""

        self.__party_nb=0
        """ The next number available to assign to a new party """

        self.__game_engine = game_engine
        """ the brain of the game """

        self.__game_engine.set__game_server(self) # set the game_server in game engine

        self.__base_board = PlayArea(width,height)
        """ the boards of each party on which the pieces, like the characters, the building, the decor's element of the game will be represented """

        self.__boards : Dict[int, PlayArea] = None
        """ the boards of each party on which the pieces, like the characters, the building, the decor's element of the game will be represented """

        self.__number_of_player_in_a_game = number_of_player_in_a_game
        """ The number of player by party """

        self.__number_of_port = number_of_port
        """ the port number from which the client will connect  """

        self.__ids = 0 # to be improved (need of login logoff system)
        """ ids that will be incremented each time a new player connects to the server  """


        ##self.__clients :

        ##self.__clients_wanting_to_play :

        ##self.__clientWaitingToBeAssigned


        self.prepare_base_board() # prepare the base board
 



    
     
    def update_party_nb(self):
        """ Update the __party_nb to prepare the next party to be ready to happen """
        self.__game_engine.set__party_nb(self.__party_nb);
        self.__game_engine.add_party();

    def analyze (msg_to_analyze : str, ip_addr : str) :
        """ 
        Analyze a msg that comes from a player
        :param msg_to_analyze msg to analyze
        :param ip_addr of the client that sends a message
        """

    def update(self, party_nb) :
        """ Send the current state of the PlayArea of a party
        :param party_nb the number of the party 
        """

    def send_to_one_client(self, ip_addr : str, msg : str, fct : int):
        """ Send a message to one player
        :param ip_addr the ip address of the registered player
        :param msg to send to the player
        :param fct that the player will have to execute 
        """
     
    def send_to_player_arriving (self, ip_address : str, msg : ByteString) :
        """ Send base board to a player arriving on the game pane
        :param ip_addr the ip address of the registered player
        :param msg  base board to send to the player 
        """


    def send_to_players_of_the_party (self, play_area_nb : int, msg : ByteString) :
        """ Send an object on its bytes form to all the players of a party
        :param play_area_nb the number of the party
        :param msg serialized form of an object to send
        """

    def send_to_players_of_the_party (self, play_area_nb : int, id : int, result : int, fct : int) :
        """ Send an object on its bytes form to all the players of a party
        :param play_area_nb the number of the party
        :param id the id of the player for which we send to message
        :param result the score or the game state (1 for gameover and 2 for victory)
        :param fct indicate the function to apply (for example, 0 to send the state of a player in the game (gameover or victory))
        """

    def prepare_base_board(self) :
        """ 
        Set the base board that every player that connects to the server will receive
        """


    def deserialize_object(byteString  : str) :
        """ 
        Deserialize an object that is of its bytes form (bytes to Object)
        :param byteString bytes form of an object
        :return the instance of an object that was deserialize (byte to Object)
        """


    def serialize_object(object  : object ) :
        """ 
        Serialize an object ( Object to bytes)
        :param object the object to transform into its bytes form
        :return bytes representing the object
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

    def set__game_engine(self, game_engine : GameEngine):
        self.__game_engine = game_engine

    def get__game_engine(self) :
        return self.__game_engine


    def set__base_board(self, base_board  : PlayArea):
        self.__base_board = base_board 

    def get__base_board(self) :
        return self.__base_board


    def set__boards(self, boards  : Dict[int,PlayArea]):
        self.__boards = boards 

    def get__boards(self) :
        return self.__boards
   

    def set__number_of_player_in_a_game(self, number_of_player_in_a_game : int):
        self.__number_of_player_in_a_game = number_of_player_in_a_game

    def get__number_of_player_in_a_game(self) :
        return self.__number_of_player_in_a_game
 

    def set__number_of_port(self, number_of_port : int):
        self.__number_of_port = number_of_port

    def get__number_of_port(self) :
        return self.__number_of_port


    def set__ids(self, ids : int):
        self.__ids = ids

    def get__ids(self) :
        return self.__ids


        ##self.__clients :

        ##self.__clients_wanting_to_play :

        ##self.__clientWaitingToBeAssigned

