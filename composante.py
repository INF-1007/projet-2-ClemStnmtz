class Composante:
    
    # TODO: Compléter la classe
    def __init__(self, nom, poids):
        self.__nom = nom
        self.__poids = poids

    @property
    def poids(self):
        return self.__poids
    @property 
    def nom(self):
        return self.__nom
    