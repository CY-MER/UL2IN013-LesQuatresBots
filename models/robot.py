"""Classe Robot"""
import math


class Robot:
    """Robot mobile"""

    def __init__(self, x: float = 0.0, y: float = 0.0, rot: int = 0,
                 rot_tete: int = 0, sens: float = 10.0):
        self.x = x
        self.y = y
        self.vitesse = 0.0
        self.rotation = rot % 360
        self.rotation_tete = rot_tete % 360
        self.portee_capteur = sens
        self._temps_restant = 0.0

    def avancer(self, distance: float, dt: float = 1.0):
        """Fait avancer le robot"""
        rad = math.radians(self.rotation)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)
        self.vitesse = distance / dt if dt > 0 else 0
        # nettoyer les erreurs de calcul
        self.x = round(self.x, 4)
        self.y = round(self.y, 4)

    def reculer(self, distance: float, dt: float = 1.0):
        """Fait reculer le robot"""
        self.avancer(-distance, dt)

    def tourner(self, angle: int):
        """Fait tourner le robot"""
        self.vitesse = 0.0
        self.rotation = (self.rotation + angle) % 360

    def tourner_tete(self, angle: int):
        """Tourne la tete du robot"""
        self.rotation_tete = (self.rotation_tete + angle) % 360

    def maj_vitesse(self, dt: float):
        """MAJ position selon vitesse"""
        if self._temps_restant <= 0:
            self.vitesse = 0.0
            return

        dt_effectif = min(dt, self._temps_restant)
        rad = math.radians(self.rotation)

        self.x += self.vitesse * math.cos(rad) * dt_effectif
        self.y += self.vitesse * math.sin(rad) * dt_effectif
        self._temps_restant -= dt_effectif

        self.x = round(self.x, 4)
        self.y = round(self.y, 4)

    def get_location(self):
        """Renvoie position du robot"""
        return self.x, self.y, self.rotation, self.vitesse

    def get_cible_capteur(self):
        """Calcule la position du capteur"""
        rotation_totale = (self.rotation + self.rotation_tete) % 360
        rad = math.radians(rotation_totale)
        cible_x = self.x + self.portee_capteur * math.cos(rad)
        cible_y = self.y + self.portee_capteur * math.sin(rad)

        return round(cible_x, 4), round(cible_y, 4)

    def __repr__(self):
        return (f"Robot(x={self.x:.2f}, y={self.y:.2f}, "
                f"rot={self.rotation}, v={self.vitesse:.2f})")
