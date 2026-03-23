"""Robot avec vecteurs"""
import math
from .vecteur2D import Vecteur2D
from .point import Point


class RobotVecteur:
    """Version avec vecteurs pour les deplacements"""

    def __init__(self, x: float = 0.0, y: float = 0.0, rot: int = 0,
                 rot_tete: int = 0, sens: float = 10.0):
        self.position = Point(x, y)
        self.rotation = rot
        self.direction = Vecteur2D(
            math.cos(math.radians(rot)),
            math.sin(math.radians(rot))
        )
        self.rotation_tete = rot_tete
        self.portee_capteur = sens
        self.vitesse = 0.0
        self._temps_restant = 0.0

    def avancer(self, dist: float, dt: float = 1.0):
        deplacement = self.direction.echelle(dist)
        self.position = self.position.ajouter(deplacement)
        self.vitesse = dist / dt
        self.position.x = round(self.position.x, 4)
        self.position.y = round(self.position.y, 4)

    def maj_vitesse(self, dt: float):
        if self._temps_restant <= 0:
            self.vitesse = 0.0
            return

        dt_eff = min(dt, self._temps_restant)
        deplacement = self.direction.echelle(self.vitesse * dt_eff)
        self.position = self.position.ajouter(deplacement)
        self._temps_restant -= dt_eff
        self.position.x = round(self.position.x, 4)
        self.position.y = round(self.position.y, 4)

    def tourner(self, angle: int):
        self.rotation = (self.rotation + angle) % 360
        self.direction = self.direction.tourne(angle)
        self.vitesse = 0.0

    def get_location(self):
        return (
            self.position.x,
            self.position.y,
            self.rotation,
            self.vitesse
        )

    def get_cible_capteur(self):
        direction_capteur = self.direction.tourne(self.rotation_tete)
        cible = self.position.ajouter(
            direction_capteur.echelle(self.portee_capteur)
        )
        return round(cible.x, 4), round(cible.y, 4)


   def points(self):
        """Retourne la liste des points du corps du robot"""
        return [(self.position.x, self.position.y)]
