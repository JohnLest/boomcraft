import xml.etree.ElementTree as ET


class Map:
    def __init__(self):
        self.hitbox_trees = []
        self.hitbox_stone = []
        self.hitbox_ore = []
        self.map = ET.parse("../resources/BoomCraft_map.xml")
        self.__set_hitbox()

    def __set_hitbox(self):
        hitbox = self.map.find("objectgroup")
        for elem in hitbox:
            type = elem.attrib.get("type")
            if type == "trees":
                self.hitbox_trees.append(elem.attrib)
            elif type == "stone":
                self.hitbox_stone.append(elem.attrib)
            elif type == "ore":
                self.hitbox_ore.append(elem.attrib)



