# step.py : calcule le mouvement du robot à chaque frame

class Step:
    def __init__(self, robot, arene, strategie):
        self.robot = robot
        self.arene = arene
        self.strategie = strategie.executer(robot)  
        self.terminee = False

    def update(self):
        """Exécute une frame de simulation."""

        if self.terminee:
            return

        try:
            # Exécute une étape de la stratégie
            next(self.strategie)
        except StopIteration:
            # La stratégie est terminée
            self.terminee = True

        # Mise à jour physique du robot
        self.robot.update()

        # Mise à jour des capteurs / raycasts
        self.robot.raycasting(self.arene)
