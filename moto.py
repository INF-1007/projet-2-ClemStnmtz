# moto.py
from vehicule import Vehicule
from specifications import MotoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Moto(Vehicule): 

    # TODO : Compléter la classe
    def __init__(self, nom, position_dep):
        moteur = Moteur(MotoSpecs.moteur_nom, 200, MotoSpecs.moteur_acceleration)
        chassis = Chassis(MotoSpecs.chassis_nom, MotoSpecs.chassis_poids, MotoSpecs.chassis_aire, MotoSpecs.chassis_trainee)
        roues = [Roue(MotoSpecs.roue_nom, MotoSpecs.roue_poids, MotoSpecs.roue_friction, MotoSpecs.roue_support) for _ in range(2)]
        super().__init__(nom, position_dep, roues, moteur, chassis, MotoSpecs, "images/moto.png")
        
       

     