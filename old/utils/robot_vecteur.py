import math
from vecteur2D import Vecteur2D
from point import Point


class RobotVecteur:
    """
    Version alternative du robot utilisant des vecteurs pour gérer
    les déplacements et les directions.
    La classe Robot classique reste utilisable pour une version simple.
    """

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        rot: int = 0,
        rot_tete: int = 0,
        sens: float = 10.0
    ):
        # Position et direction
        self.position = Point(x, y)
        self.rotation = rot
        self.direction = Vecteur2D(
            math.cos(math.radians(rot)),
            math.sin(math.radians(rot))
        )

        # Paramètres du robot
        self.rotation_tete = rot_tete
        self.portee_capteur = sens
        self.vitesse = 0.0

        # Gestion du temps de déplacement
        self._temps_restant = 0.0

    def avancer(self, dist: float, dt: float = 1.0):
        """Fait avancer le robot dans la direction actuelle"""
        deplacement = self.direction.echelle(dist)
        self.position = self.position.ajouter(deplacement)

        self.vitesse = dist / dt

        # Nettoyage 
        self.position.x = round(self.position.x, 4)
        self.position.y = round(self.position.y, 4)

    def maj_vitesse(self, dt: float):
        """Met à jour la position en fonction de la vitesse et du temps"""
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
        """Fait tourner le robot d'un angle donné"""
        self.rotation = (self.rotation + angle) % 360
        self.direction = self.direction.tourne(angle)
        self.vitesse = 0.0

    def get_location(self):
        """Renvoie la position, l'orientation et la vitesse du robot"""
        return (
            self.position.x,
            self.position.y,
            self.rotation,
            self.vitesse
        )

    def get_cible_capteur(self):
        """Renvoie la position ciblée par le capteur"""
        direction_capteur = self.direction.tourne(self.rotation_tete)
        cible = self.position.ajouter(
            direction_capteur.echelle(self.portee_capteur)
        )

        return round(cible.x, 4), round(cible.y, 4)
