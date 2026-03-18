class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Crée un point en coordonnées cartésiennes"""
        self.x = x
        self.y = y

    def copie(self):
        """Retourne une copie indépendante du point"""
        return Point(self.x, self.y)

    def deplacer(self, vecteur):
        """Déplace le point à l'aide d'un vecteur"""
        self.x += vecteur.dx
        self.y += vecteur.dy
        return self

    def ajouter(self, vecteur):
        """Retourne un nouveau point après déplacement"""
        return Point(self.x + vecteur.dx, self.y + vecteur.dy)

    def distance(self, autre) -> float:
        """Calcule la distance entre deux points"""
        dx = self.x - autre.x
        dy = self.y - autre.y
        return (dx ** 2 + dy ** 2) ** 0.5
