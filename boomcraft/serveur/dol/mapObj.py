import xml.etree.ElementTree as ET
from dol.resourcesObj import ResourcesObj as Resources


class MapObj:
    def __init__(self):
        self.lst_trees = []
        self.lst_stone = []
        self.lst_ore = []
        self.map = ET.parse("./resources/BoomCraft_map.xml")
        self.__init_list()

    def __init_list(self):
        hitbox = self.map.find("objectgroup")
        for elem in hitbox:
            type = elem.attrib.get("type")
            x = int(elem.attrib.get("x") or 0)
            y = int(elem.attrib.get("y") or 0)
            width = int(elem.attrib.get("width") or 0)
            height = int(elem.attrib.get("height") or 0)
            resource = Resources(type, x, y, width, height)
            resource.set_hitbox()
            if type == "trees":
                self.lst_trees.append(resource)
            elif type == "stone":
                self.lst_stone.append(resource)
            elif type == "ore":
                self.lst_ore.append(resource)



