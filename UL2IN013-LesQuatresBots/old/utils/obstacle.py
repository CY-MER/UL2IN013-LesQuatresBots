from point import Point
import math

class Obstacle:
    """ Obstacle simple pouvant être un rectangle, un cercle ou un triangle """
    def __init__(self, type_, data):
        self.type = type_       # type_: "rectangle", "cercle", "triangle"
        self.data = data        # data_: coordonnées et dimensions selon le type

    def collision(self, robot):
        """Retourne True si le robot touche l'obstacle"""
        for px, py in robot.points():
            if self.type == "rectangle":
                x, y, largeur, hauteur = self.data
                # Vérifie si le point est à l'intérieur du rectangle 
                if x <= px <= x + largeur and y <= py <= y + hauteur:
                    return True  # Collision détectée

            elif self.type == "cercle":
                cx, cy, rayon = self.data
                # Calcul de la distance entre le point et le centre 
                if math.hypot(px - cx, py - cy) <= rayon:
                    return True  # Si la distance est inférieure ou égale au rayon : collision

            elif self.type == "triangle":
                p1, p2, p3 = self.data   # les trois sommets du triangle
                # On calcule de quel côté de chaque ligne du triangle est le point
                d1 = self._signe((px, py), p1, p2)
                d2 = self._signe((px, py), p2, p3)
                d3 = self._signe((px, py), p3, p1)
                # Vérifie si le point est à l'intérieur du triangle
                has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)   # côté négatif
                has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)   # côté positif
                if not (has_neg and has_pos):
                    return True   # Si le point n'est pas des deux côtés : collision
        return False
    def _signe(self, p1, p2, p3):
        """Fonction pour vérifier point dans triangle"""
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])

