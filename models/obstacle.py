import math
from .point import Point


class Obstacle:
    """ Obstacle : rectangle, cercle ou triangle """
    def __init__(self, type_obj, data, couleur=(120,120,120)):
        self.type = type_obj   # "rectangle", "cercle", "triangle"
        self.data = data
        self.couleur = couleur

    def collision(self, robot):
        """ Retourne True si un des points du robot est dans l'obstacle """
        px, py, _, _ = robot.get_location()
      

        if self.type == "rectangle":
            x, y, large, haut = self.data
            if x <= px <= x + large and y <= py <= y + haut:
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
                
            # Si les trois signes sont identiques, le point est dedans
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            if not (has_neg and has_pos):
                return True
                    
        return False

    def _signe(self, p1, p2, p3):
        """ Calcule l'orientation du triangle formé par p1, p2, p3 """
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
