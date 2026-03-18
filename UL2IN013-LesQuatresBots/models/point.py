class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def copie(self):
        return Point(self.x, self.y)

    def deplacer(self, vecteur):
        self.x += vecteur.dx
        self.y += vecteur.dy
        return self

    def ajouter(self, vecteur):
        return Point(self.x + vecteur.dx, self.y + vecteur.dy)

    def distance(self, autre) -> float:
        dx = self.x - autre.x
        dy = self.y - autre.y
        return (dx ** 2 + dy ** 2) ** 0.5
