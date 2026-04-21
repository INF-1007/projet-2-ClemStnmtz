from vehicule import Vehicule
from specifications import AutoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Auto(Vehicule):


    # TODO : Compléter la classe    
    def __init__(self, nom, position_dep):
        
        moteur = Moteur(AutoSpecs.moteur_nom, 300, AutoSpecs.moteur_acceleration)
        chassis = Chassis(AutoSpecs.chassis_nom, AutoSpecs.chassis_poids, AutoSpecs.chassis_aire, AutoSpecs.chassis_trainee)
        roues = [Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support) for _ in range(4)]
        super().__init__(nom, position_dep, roues, moteur, chassis, AutoSpecs, "images/auto.png")