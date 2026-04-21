import random
import pygame
from config import WIDTH, HEIGHT

class Confetti: 
    

    # TODO : Compléter la classe
    def __init__(self):
        self.taille = random.randint(5, 10)
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.vitesse = random.uniform(2, 5)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def tomber(self):
        self.y += self.vitesse

    def dessiner(self, screen):
        if self.y < HEIGHT:
            pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.taille, self.taille))