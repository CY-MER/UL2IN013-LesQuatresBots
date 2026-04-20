import math


class Vecteur2D:
    def __init__(self, dx: float = 0.0, dy: float = 0.0):
        self.dx = dx
        self.dy = dy

    def copie(self):
        return Vecteur2D(self.dx, self.dy)

    def est_egal(self, autre) -> bool:
        return self.dx == autre.dx and self.dy == autre.dy

    def ajouter(self, autre):
        return Vecteur2D(self.dx + autre.dx, self.dy + autre.dy)

    def retirer(self, autre):
        return Vecteur2D(self.dx - autre.dx, self.dy - autre.dy)

    def echelle(self, facteur: float):
        return Vecteur2D(self.dx * facteur, self.dy * facteur)

    def longueur(self) -> float:
        return math.hypot(self.dx, self.dy)

    def normalise(self):
        n = self.longueur()
        if n == 0:
            return Vecteur2D(0, 0)
        return Vecteur2D(self.dx / n, self.dy / n)

    def tourne(self, degres: float):
        angle = math.radians(degres)
        return Vecteur2D(
            self.dx * math.cos(angle) - self.dy * math.sin(angle),
            self.dx * math.sin(angle) + self.dy * math.cos(angle)
        )

    def scalaire(self, autre) -> float:
        return self.dx * autre.dx + self.dy * autre.dy

    def determinant(self, autre) -> float:
        return self.dx * autre.dy - self.dy * autre.dx
