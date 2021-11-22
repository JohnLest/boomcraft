class GameClient:
    def __init__(self, position=0):
        self._position = position

    def avance(self, distance=1):
        self._position+= distance
        print("Avance de", distance)

    def getPosition(self):
        return self._position
