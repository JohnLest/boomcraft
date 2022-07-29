from dol.dictionaryObj import DictionaryObj
from dol.forumObj import ForumObj as Forum

class BuildingService:
    def __init__(self):
        self.__dictionary_forum = DictionaryObj()

    def create_forum(self, id_player, x, y):
        new_forum = Forum(id_player, x=x, y=y)
        self.__dictionary_forum.insert(new_forum.id, new_forum)

    def get_all_forum_by_id_player(self, id_player):
        return self.__dictionary_forum.get_all_filter("id_owner", id_player)
