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


class Carre(Strategie):
    """Fait faire un carré au robot"""

    def __init__(self, cote, pas=5, pas_angle=5):
        self.cote = cote
        self.pas = pas
        self.pas_angle = pas_angle
        self.cote_actuel = 0
        self.phase = "avance"
        self.strategie_courante = Avancer(cote, pas)
        self.terminee = False
        
    def update(self, robot, obstacles=None):
        if self.terminee:
            return

        self.strategie_courante.update(robot, obstacles)

        if self.strategie_courante.terminee:
            if self.phase == "avance":
                self.phase = "tourne"
                self.strategie_courante = Tourner(90, self.pas_angle)
            elif self.phase == "tourne":
                self.cote_actuel += 1
                if self.cote_actuel >= 4:
                    self.terminee = True
                else:
                    self.phase = "avance"
                    self.strategie_courante = Avancer(self.cote, self.pas)
