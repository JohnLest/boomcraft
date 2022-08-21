from typing import List
import logging


class DictionaryObj:
    def __init__(self):
        self.__dict_obj = {}
        self.logger = logging.getLogger(__name__)

    def insert(self, id, obj):
        self.__dict_obj.update({id: obj})

    def get_by_id(self, id):
        return self.__dict_obj.get(id)

    def get_first(self, attribute, filter):
        for _key, _value in self.__dict_obj.items():
            if getattr(_value, attribute) == filter:
                return _value

    def get_all(self) -> dict:
        return self.__dict_obj

    def get_all_filter(self, attribute, filter) -> List:
        match = []
        for _key, _value in self.__dict_obj.items():
            if getattr(_value, attribute) == filter:
                match.append(_value)
        return match

    def get_attribute(self, attribute_return, attribute_filter=None, filter=None) -> List:
        match =[]
        for _key, _value in self.__dict_obj.items():
            if filter is None:
                match.append(getattr(_value, attribute_return))
            elif getattr(_value, attribute_filter) == filter:
                match.append(getattr(_value, attribute_return))
        return match

    def delete(self, id):
        try:
            self.__dict_obj.pop(id)
        except Exception as ex:
            self.logger.error(f"error delete() : {ex.args[0]}")
