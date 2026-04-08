"""Robot avec vecteurs"""
import math
from .vecteur2D import Vecteur2D
from .point import Point


class Robot:
    """Version avec vecteurs pour les deplacements"""

    def __init__(self, x: float = 0.0, y: float = 0.0, rot: int = 0,
                 rot_tete: int = 0, sens: float = 10.0):
        self.position = Point(x, y)
        self.dessine = False
        self.couleur = (255,0,0)
        self.rotation = rot % 360
        self.direction = Vecteur2D(
            math.cos(math.radians(rot)),
            math.sin(math.radians(rot))
        )
        self.rotation_tete = rot_tete
        self.portee_capteur = sens

        self.vitesse = 0.0
        self.vitesse_rd = 0.0
        self.vitesse_rg = 0.0

    def avancer(self, vitesse: float):
        """ commande d'anvance : les deux roues a la meme vitesse """
        self.vitesse_rd = vitesse
        self.vitesse_rg = vitesse 

    def tourner(self, vitesse: float):
        """commande de rotation : les deux roues a des vitesses opposées"""
        self.vitesse_rd = -vitesse 
        self.vitesse_rg = vitesse 

    def stop (self):
        """arrete du robot : vitesse des roues nulle """
        self.vitesse_rd = 0.0
        self.vitesse_rg = 0.0
        self.vitesse = 0.0

    def set_vitesse_roues(self, vg:float , vd:float):
        self.vitesse_rd = vd
        self.vitesse_rg = vg

    def update(self, dt:float=1.0):
        """mise a jour de la positio et la rotation selon les vitesses des roues"""
        self.vitesse = (self.vitesse_rd + self.vitesse_rg) / 2

        rotation_change = (self.vitesse_rg - self.vitesse_rd) * dt * 2 # transforme la difference entre les roues en rotation du robot 
        self.rotation =(self.rotation +rotation_change) % 360

        self.direction = Vecteur2D( 
            math.cos(math.radians(self.rotation)),
            math.sin(math.radians(self.rotation))
         )
        deplacement = self.direction.echelle(self.vitesse * dt)
        self.position = self.position.ajouter(deplacement)

        self.position.x = round(self.position.x, 4)
        self.position.y = round(self.position.y, 4)

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
        """retourne la liste des points du corps du robot"""
        return [(self.position.x, self.position.y)]


    def set_dessine(self, b: bool):
        self.dessine = b


    def change_couleur(self, c):
        self.couleur = c


