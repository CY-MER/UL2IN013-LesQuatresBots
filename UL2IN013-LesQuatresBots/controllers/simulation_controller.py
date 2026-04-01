from models import Robot 
from models.obstacle import Obstacle 

class SimulationController: 
    """gère uniquement l'etat et l'evolution de la simulation"""

    def __init__(self, width=400, height=400):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """Réinitialise la simulation"""
        self.robot = Robot(self.width // 2, self.height // 2)
        self.points = [(self.robot.x, self.robot.y)]


        self.obstacles = [
            Obstacle("cercle", (100, 100, 20)),
            Obstacle("rectangle", (180, 290, 60, 30)),
            Obstacle("triangle", ((300, 300), (340, 260), (360, 320))),
        ]

        # paramètres du carré
        self.cote = 100
        self.steps = 40
        self.side = 0
        self.step = 0
        self.en_pause_rotation = False

    def update(self):
        """Met à jour la simulation"""
        if self.side >= 4:
            return

        if self.step == 0 and not self.en_pause_rotation:
            self.robot.tourner(90)
            self.robot.vitesse = 0.0
            self.en_pause_rotation = True

        elif self.en_pause_rotation:
            self.en_pause_rotation = False
            self.step = 1

       elif self.step < self.steps:
            distance = self.cote / self.steps

            #vérifier la collision 
            old_x, old_y, _, _ = self.robot.get_location()
            self.robot.avancer(distance, dt=1.0)
            for obstacle in self.obstacles:
                if obstacle.collision(self.robot):
                    self.robot.x = old_x
                    self.robot.y = old_y
                    self.robot.vitesse = 0
                    self.robot.tourner(180)
                    print("Collision !")
                    return 
        
            self.points.append((self.robot.x, self.robot.y))
            self.step += 1

    def get_robot_info(self):
        """Retourne les infos utiles pour l'affichage"""
        x, y, angle, vitesse = self.robot.get_location()
        return {
            "x": x,
            "y": y,
            "angle": angle,
            "vitesse": vitesse,
            "points": self.points,
            "obstacles": self.obstacles,
        }
