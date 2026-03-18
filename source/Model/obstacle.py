# obstacle.py : gere les obstacles dans la simulation
from Model.vecteur import Vecteur

class Polygone:
    def __init__(self, points:list[Vecteur]):
        """ Initialisation du polygone, défini par une liste de points """
        self.points = points
    
    def get_points(self):
        """ Renvoie les points du polygone dans l'ordre """
        return self.points
