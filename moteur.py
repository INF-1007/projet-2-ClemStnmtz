from composante import Composante

class Moteur(Composante):
    # TODO : Compléter la classe
    def __init__(self,nom, poids, acceleration):
         super().__init__(nom, poids)
         self.__acceleration= acceleration

    @property
    def acceleration(self):
         return self.__acceleration
         