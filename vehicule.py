import numpy as np
import pygame
from specifications import DENSITE_AIR

# TODO : Créer la classe Vehicule

class Vehicule:
    def __init__(self, nom, position, vitesse, roues, moteur, chassis, poids_total):
        self.__nom=nom
        self.__position=np.array(position, dtype=float)
        self.__vitesse=np.array([0,0], dtype=float)
        self.__roues=roues
        self.__moteur=moteur 
        self.__chassis=chassis
        
        
    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):

        # TODO : ajouter les attributs
        self.__nom = nom
        self.__position = np.array(position_dep, dtype=float)
        self.__vitesse = np.array([0.0, 0.0], dtype=float)
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis

        
        self.__poids_total=self.calculer_poids_total()

        # TODO : ajouter un attribut pour l'image du véhicule
        self.image = None
        self.taille_image = (Specs.image_width, Specs.image_height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, self.taille_image)
        
        

    @property
    def nom(self):
        return self.__nom
    @property
    def position(self):
        return self.__position
    @property
    def vitesse(self):
        return self.__vitesse
    @property
    def poids_total(self):
        return self.__poids_total

    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode 
        screen.blit(self.image, (self.__position[0] - self.taille_image[0], self.__position[1]))
        #alignement de l'image pour que l'arriere soit à la position x (pour la ligne de départ)
        
    
    def calculer_poids_total(self):
        # TODO : compléter la méthode
        poids_composantes = self.__moteur.poids + self.__chassis.poids
        poids_roues = sum(roue.poids for roue in self.__roues)
        return poids_composantes + poids_roues

    def calculer_traction(self):
        # TODO : compléter la méthode 
        # Traction = poids_total * acceleration_moteur
        return self.__poids_total * self.__moteur.acceleration

    def calculer_friction(self):
        # TODO : compléter la méthode 
        # Somme des (coefficient_friction * vitesse_x) pour chaque roue
        return sum(roue.coefficient_friction * self.__vitesse[0] for roue in self.__roues)

    def calculer_trainee(self):
        # TODO : compléter la méthode 
        # 1/2 * coefficient_trainee * aire_frontale * densite_air * vitesse^2
        v_x = self.__vitesse[0]
        return 0.5 * self.__chassis.coefficient_trainee * self.__chassis.aire_frontale * DENSITE_AIR * (v_x**2)

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        traction = self.calculer_traction()
        trainee = self.calculer_trainee()
        friction = self.calculer_friction()
        
        # Force résultante / masse
        accel_x = (traction - trainee - friction) / self.__poids_total
        
        # Mise à jour vitesse et position (Euler simple)
        self.__vitesse[0] += accel_x * dt
        self.__position += self.__vitesse * dt

    def celebrer(self):
        # TODO : compléter la méthode 
        return f"{self.__nom} remporte la course !"