import math

class Strategie:
    """Classe de base pour les stratégies"""

    def update(self, robot):
        pass


class Avancer(Strategie):
    """Fait avancer le robot d'une distance donnée, petit à petit"""

    def __init__(self, distance, pas=5):
        self.distance = distance
        self.pas = pas
        self.positions_depart = None 

    def update(self, robot, dt):
        if self.positions_depart is None:
            self.positions_depart = (robot.position.x , robot.position.y)

        x0 ,y0 = self.positions_depart
        x , y = robot.position.x , robot.posotion.y

        distance_parcourue = math.sqrt((x-x0)**2 + (y-y0)**2)

        if distance_parcourue >= self.distance:
            robot.stop()
            return 
        
        robot.avancer(self.vitesse)
        

class Tourner(Strategie):
    """Fait tourner le robot d'un angle donné, petit à petit"""

    def __init__(self, angle, vitesse):
        self.angle = angle
        self.vitesse = vitesse
        self.rotation_depart = None 

    def update(self, robot):
        if self.position_depart is None :
            self.rotation_depart = (robot.rotation)

        rotation = abs(robot.rotation - self.rotation_depart)

        if rotation >= self.angle:
            robot.stop()
            return 
        
        robot.tourner(self.vitesse)

class Stop(Strategie):
    """Arrête le robot"""

    def update(self, robot):
        robot.stop()


class StratSequence(Strategie):
    """ Execute une liste de strategie de maniére séquentielle """
    def __init__(self, strategies):
        self.strategies = strategies
        self.index = 0

    def start(self, robot):
        self.index = 0
        if self.strategies:
            self.strategies[0].start(robot)

    def update(self, robot):
        # verifier si les strategies sont terminés 
        if self.fini():
            return
        
        strat = self.strategies[self.index]
        strat.update(robot)

        if strat.fini():
            self.index += 1
            if not self.fini():
                self.strategies[self.index].start(robot)

    def fini(self):
        return self.index >= len(self.strategies)



class Carre(StratSequence):
    """ fait un carré"""
    def __init__(self,cote):
        strategies = [
            Avancer(cote),
            Tourner(90),
            Avancer(cote),
            Tourner(90),
            Avancer(cote),
            Tourner(90),
            Avancer(cote),
            Tourner(90),
        ]
        super().__init__(strategies)


