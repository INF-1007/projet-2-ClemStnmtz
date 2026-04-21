### Raisonnement pour l'implémentation des confettis

#### 1. Modélisation d'un objet unique (`Confetti`)
j'ai créé une classe Confetti dans `confettis.py` pour encapsuler les propriétés de chaque particule :
- Pour éviter un effet monotone, chaque confetti reçoit une couleur aléatoire via `random.randint` pour le RGB, une taille variée et une vitesse de chute différente.
- Position de départ : Ils apparaissent à une coordonnée `x` aléatoire sur toute la largeur de l'écran (`WIDTH`) et à une coordonnée `y` négative pour qu'ils semblent tomber du "ciel" plutôt que d'apparaître subitement au milieu de l'écran.

#### 2. Gestion du mouvement et de l'affichage
- Méthode `tomber()` : À chaque frame de la simulation, on incrémente la position `y` de l'objet par sa `vitesse` propre, certains confettis tombent plus vite que d'autres.
- Méthode `dessiner()` : On utilise `pygame.draw.rect` pour dessiner un carré, pour respecter la contrainte de forme imposée par le sujet.

#### 3. Coordination avec la fin de la course (dans `main.py`)
Le défi était de déclencher l'animation au bon moment :
- La liste de confettis n'est générée qu'une seule fois, au moment précis où le premier véhicule dépasse `FINISH_LINE_X`.
- Une fois le gagnant identifié, le programme parcourt la liste des confettis à chaque itération de la boucle `while running` pour appeler leurs méthodes respectives.
- Les confettis ne sont calculés et affichés que si la variable `gagnant` n'est plus `None`, évitant ainsi de charger le processeur inutilement pendant la course.

#### 4. Choix techniques
- J'ai choisi de générer 100 confettis pour obtenir un effet festif sans ralentir la simulation.