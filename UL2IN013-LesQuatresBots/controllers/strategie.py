class Strategie:
    """Classe de base pour les stratégies"""

    def update(self, robot):
        pass


class Avancer(Strategie):
    """Fait avancer le robot d'une distance donnée, petit à petit"""

    def __init__(self, distance, pas=5):
        self.distance = distance
        self.pas = pas
        self.distance_parcourue = 0
        self.terminee = False

    def update(self, robot):
        if self.terminee:
            return

        if self.distance_parcourue < self.distance:
            deplacement = min(self.pas, self.distance - self.distance_parcourue)
            robot.avancer(deplacement)
            self.distance_parcourue += deplacement
        else:
            self.terminee = True


class Tourner(Strategie):
    """Fait tourner le robot d'un angle donné, petit à petit"""

    def __init__(self, angle, pas_angle=5):
        self.angle = angle
        self.pas_angle = pas_angle
        self.angle_tourne = 0
        self.terminee = False

    def update(self, robot):
        if self.terminee:
            return

        if self.angle_tourne < self.angle:
            rotation = min(self.pas_angle, self.angle - self.angle_tourne)
            robot.tourner(rotation)
            self.angle_tourne += rotation
        else:
            self.terminee = True


class Stop(Strategie):
    """Arrête le robot"""

    def __init__(self):
        self.terminee = False

    def update(self, robot):
        robot.vitesse = 0
        self.terminee = True


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

    def update(self, robot):
        if self.terminee:
            return

        self.strategie_courante.update(robot)

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