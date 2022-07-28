from typing import List


class DictionaryObj:
    def __init__(self):
        self.__dict_obj = {}

    def insert(self, id, obj):
        self.__dict_obj.update({id: obj})

    def get_by_id(self, id):
        return self.__dict_obj.get(id)

    def get_first(self, attribute, filter):
        for _key, _value in self.__dict_obj.items():
            if getattr(_value, attribute) == filter:
                return _value

    def get_all(self):
        return self.__dict_obj

    def get_all_filter(self, attribute, filter) -> List:
        match = []
        for _key, _value in self.__dict_obj.items():
            if getattr(_value, attribute) == filter:
                match.append(_value)
        return match

    def delete(self, id):
        self.__dict_obj.pop(id)
