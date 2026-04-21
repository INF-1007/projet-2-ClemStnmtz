from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 

    # TODO : Compléter la classe
    def __init__(self, nom, position_dep):
        moteur = Moteur(CamionSpecs.moteur_nom, 600, CamionSpecs.moteur_acceleration)
        chassis = Chassis(CamionSpecs.chassis_nom, CamionSpecs.chassis_poids, CamionSpecs.chassis_aire, CamionSpecs.chassis_trainee)
        roues = [Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support) for _ in range(6)]
        super().__init__(nom, position_dep, roues, moteur, chassis, CamionSpecs, "images/camion.png")
        