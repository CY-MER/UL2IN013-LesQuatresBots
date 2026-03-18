# Robot.py : définition de la classe Robot
import math

class Robot:
    def __init__(self, x:float=0.0, y:float=0.0, rot:int=0, rot_tete:int=0, sens:float=10.0):
        """ Initialisation du robot"""
        self.x = x
        self.y = y
        self.vitesse = 0.0
        self.rotation = rot # rotation du corps du robot
        self.rotation_tete = rot_tete # rotation de la tete par rapport au corps
        self.portee_capteur = sens # porte du capteur

    def avancer(self, dist:float, dt: float = 1.0):
        """ fait avancer le robot dans la direction de sa rotation """
        rad = math.radians(self.rotation)
        self.x += dist * math.cos(rad)
        self.y += dist * math.sin(rad)
        
        # vitesse 

    def maj_vitesse(self, dt):
        if self._temps_restant <= 0:
            self.vitesse = 0
            return

        dt_effectif = min(dt, self._temps_restant)

        rad = math.radians(self.rotation)

        self.x += self.vitesse * math.cos(rad) * dt_effectif
        self.y += self.vitesse * math.sin(rad) * dt_effectif

        self._temps_restant -= dt_effectif

        # arrondir pour nettoyer les micro-erreurs de calcul sur flottant
        self.x = round(self.x, 4)
        self.y = round(self.y, 4)

    def tourner(self, a:int):
        self.vitesse = 0.0
        """ fait tourner le robot d'un angle a """
        self.rotation = (self.rotation + a) % 360

    def get_location(self):
        """ renvoie la position et l'orientation du robot """
        return self.x, self.y, self.rotation, self.vitesse
    
    def get_cible_capteur(self):
        """ renvoie la position regarde par le capteur en fonction de la rotation du robot et celle de sa tete """
        rotation_totale = (self.rotation + self.rotation_tete) % 360
        rad = math.radians(rotation_totale)
        cible_x = self.x + self.portee_capteur * math.cos(rad)
        cible_y = self.y + self.portee_capteur * math.sin(rad)

        # meme nettoyage
        cible_x = round(cible_x, 4)
        cible_y = round(cible_y, 4)

        return cible_x, cible_y
