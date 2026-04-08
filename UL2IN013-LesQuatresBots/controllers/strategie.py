import math

class Strategie:
    """Classe de base pour les stratégies"""

    def update(self, robot):
        pass


class Avancer(Strategie):
    """Fait avancer le robot d'une distance donnée, petit à petit"""

    def __init__(self, distance, pas=2):
        self.distance = distance
        self.pas = pas
        self.position_depart = None 
        self.distance_parcourue = 0.0

    def update(self, robot):
        if self.position_depart is None:
            self.position_depart = (robot.position.x , robot.position.y)

        x0 ,y0 = self.position_depart
        x , y = robot.position.x , robot.position.y

        self.distance_parcourue = math.sqrt((x-x0)**2 + (y-y0)**2)

        if self.distance_parcourue >= self.distance:
            robot.stop()
            return 
        
        robot.avancer(self.pas)

    def fini(self):
        return self.distance_parcourue >= self.distance 

class Tourner(Strategie):
    """Fait tourner le robot d'un angle donné, petit à petit"""

    def __init__(self, angle, vitesse=0.3):
        self.angle = angle
        self.vitesse = vitesse
        self.rotation_depart = None 
        self.rotationfinale = 0.0

    def update(self, robot):
        if self.rotation_depart is None :
            self.rotation_depart = (robot.rotation)

        self.rotationfinale = (robot.rotation - self.rotation_depart) % 360

        if self.rotationfinale >= self.angle:
            robot.stop()
            return 
        
        robot.tourner(self.vitesse)

    def fini(self):
        return self.rotationfinale >= self.angle
        
    

class Stop(Strategie):
    """Arrête le robot"""

    def update(self, robot):
        robot.stop()


class StratSequence(Strategie):
    """ Execute une liste de strategie de maniére séquentielle """
    def __init__(self, strategies):
        self.strategies = strategies
        self.index = 0

    def update(self, robot):
        # verifier si les strategies sont terminés 
        if self.fini():
            return
        
        strat = self.strategies[self.index]
        strat.update(robot)

        if strat.fini():
            self.index += 1

    def fini(self):
        return self.index >= len(self.strategies)


#  NOUVELLE STRATÉGIE : HEXAGONE
class Hexagone(Strategie):
    """Dessine un hexagone avec une couleur différente à chaque côté"""

    def __init__(self, longueur, couleurs):
        self.longueur = longueur
        self.couleurs = couleurs
        self.cote = 0
        self.sous_strat = None

    def update(self, robot):
        if self.sous_strat is None:
            if self.cote >= 6:
                robot.stop()
                return

            # changement de couleur
            robot.change_couleur(self.couleurs[self.cote])

            # avancer + tourner
            self.sous_strat = StratSequence([
                Avancer(self.longueur),
                Tourner(60)
            ])

        self.sous_strat.update(robot)

        if self.sous_strat.fini():
            self.cote += 1
            self.sous_strat = None

    def fini(self):
        return self.cote >= 6