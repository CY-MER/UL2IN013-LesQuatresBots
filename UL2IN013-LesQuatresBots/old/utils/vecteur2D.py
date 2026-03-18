import math

class Vecteur2D:
    def __init__(self, dx: float = 0.0, dy: float = 0.0):
        """Crée un vecteur 2D"""
        self.dx = dx
        self.dy = dy

    def copie(self):
        """Retourne une copie indépendante du vecteur"""
        return Vecteur2D(self.dx, self.dy)

    def est_egal(self, autre) -> bool:
        """Teste l'égalité entre deux vecteurs"""
        return self.dx == autre.dx and self.dy == autre.dy

    def ajouter(self, autre):
        """Addition vectorielle"""
        return Vecteur2D(self.dx + autre.dx, self.dy + autre.dy)

    def retirer(self, autre):
        """Soustraction vectorielle"""
        return Vecteur2D(self.dx - autre.dx, self.dy - autre.dy)

    def echelle(self, facteur: float):
        """Multiplie le vecteur par un scalaire"""
        return Vecteur2D(self.dx * facteur, self.dy * facteur)

    def longueur(self) -> float:
        """Longueur """
        return math.hypot(self.dx, self.dy)

    def normalise(self):
        """Retourne un vecteur unitaire """
        n = self.longueur()
        if n == 0:
            return Vecteur2D(0, 0)
        return Vecteur2D(self.dx / n, self.dy / n)

    def tourne(self, degres: float):
        """Fait tourner le vecteur d'un angle donné """
        angle = math.radians(degres)
        return Vecteur2D(
            self.dx * math.cos(angle) - self.dy * math.sin(angle),
            self.dx * math.sin(angle) + self.dy * math.cos(angle)
        )

    def scalaire(self, autre) -> float:
        """Produit scalaire"""
        return self.dx * autre.dx + self.dy * autre.dy

    def determinant(self, autre) -> float:
        """Déterminant (équivalent du produit vectoriel en 2D)"""
        return self.dx * autre.dy - self.dy * autre.dx
