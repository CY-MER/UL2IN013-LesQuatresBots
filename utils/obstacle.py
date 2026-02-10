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
                if x <= px <= x + largeur and y <= py <= y + hauteur:
                    return True

            elif self.type == "cercle":
                cx, cy, rayon = self.data
                if math.hypot(px - cx, py - cy) <= rayon:
                    return True

            elif self.type == "triangle":
                p1, p2, p3 = self.data
                d1 = self._signe((px, py), p1, p2)
                d2 = self._signe((px, py), p2, p3)
                d3 = self._signe((px, py), p3, p1)
                has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
                has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
                if not (has_neg and has_pos):
                    return True
        return False
