class GameClient:
    def __init__(self, position=0):
        self._position = position

    def avance(self, distance=1):
        self._position+= distance
        print("Avance de", distance)

    def getPosition(self):
        return self._position


class Ecran:
    global nb_ecrans
    nb_ecrans=0
    def __init__(self,t="Inconnu",mg="Inconnu",mdl="Inconnu"):
        print("constructeur par défaut ou  3 arguments")
        self.type=t
        self.marque=mg
        self.modele=mdl
        self.nb_ecrans=nb_ecrans+1

    def modif_type(self,mod):
        tmod=["CRT","LCD","PLASMA"]
        ok=False
        for i in range(0,len(tmod)):
            if mod==tmod[i]:
                ok=True

    def affiche_type(self):
        print("type : ", self.type)

    def nbEcrans(self):
        print("nombre ecrans (fonction) :",nb_ecrans)

o1=Ecran("LCD","LG","L19155")
o1.affiche_type()
Ecran.nbEcrans(1)
print("nombre ecran (main):",o1.nb_ecrans)