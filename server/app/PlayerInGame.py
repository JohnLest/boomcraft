from app.PlayerInfo import PlayerInfo

class PlayerInGame :
    
    def __init__(self, player_info : PlayerInfo, play_area_nb : int ):
        
        self.__player_info = player_info

        self.__game_over = False

        self.__won = False

        self.__play_area_nb = -1



    def set__player_info(self,player_info : PlayerInfo):
        self.__player_info = player_info

    def get__player_info(self) :
        return self.__player_info


    def set__game_over(self,game_over : bool):
        self.__game_over = game_over

    def get__game_over(self) :
        return self.__game_over


    def set__won(self,won : bool):
        self.__won = won

    def get__won(self) :
        return self.__won


    def set__play_area_nb(self,play_area_nb : int):
        self.__play_area_nb = play_area_nb

    def get__play_area_nb(self) :
        return self.__play_area_nb