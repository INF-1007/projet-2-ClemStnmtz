from composante import Composante

# TODO : Créer la classe Roue

class Roue(Composante):
    # TODO : Compléter la classe
    def __init__(self,nom, poids, coefficient_friction,poids_supporte):
         super().__init__(nom, poids)
         self.__coefficient_friction=coefficient_friction
         self.__poids_supporte=poids_supporte

    @property 
    def coefficient_friction(self):
         return self.__coefficient_friction

    @property 
    def poids_supporte(self):
         return self.__poids_supporte

