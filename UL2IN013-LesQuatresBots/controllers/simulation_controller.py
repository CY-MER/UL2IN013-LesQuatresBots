from models import Robot 
from models.obstacle import Obstacle 
from .strategie import StratSequence, Stop , Avancer , Tourner  , Hexagone

class SimulationController: 
    """gère uniquement l'etat et l'evolution de la simulation"""

    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """Réinitialise la simulation"""
        self.robot = Robot(self.width // 2, self.height // 2)
        self.points = [(self.robot.position.x, self.robot.position.y)]


        self.obstacles = [
            Obstacle("cercle", (200, 300, 20), couleur=(255,0,0)),# rouge
            Obstacle("cercle", (200, 100, 20), couleur=(0,255,0)),# vert
            Obstacle("cercle", (200, 200, 20), couleur=(0,0,255)),# bleu
        ]

   
      

        self.robot1 = Robot(self.width - 50, self.height // 2)  # à droite
        self.robot2 = Robot(50, self.height // 2)               # à gauche


        self.strategie1 = StratSequence([
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            ])

        self.strategie2 = Hexagone( 
            longueur=50,
            couleurs=[
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 255, 0),
            (0, 255, 255)
            
        ])



    def update(self):
        old_x1, old_y1 = self.robot1.position.x, self.robot1.position.y
        old_x2, old_y2 = self.robot2.position.x, self.robot2.position.y

    # mise à jour indépendante
    self.strategie1.update(self.robot1)
    self.strategie2.update(self.robot2)

    self.robot1.update()
    self.robot2.update()

    # gestion collisions (robot1)
    for obstacle in self.obstacles:
        if obstacle.collision(self.robot1):
            self.robot1.position.x = old_x1
            self.robot1.position.y = old_y1
            self.robot1.stop()
            self.strategie1 = Stop()
            print("Collision robot 1")
            return

    # gestion collisions (robot2)
    for obstacle in self.obstacles:
        if obstacle.collision(self.robot2):
            self.robot2.position.x = old_x2
            self.robot2.position.y = old_y2
            self.robot2.stop()
            self.strategie2 = Stop()
            print("Collision robot 2")
            return

    if self.robot1.dessine:
        self.points1.append((self.robot1.position.x, self.robot1.position.y))

    if self.robot2.dessine:
        self.points2.append((self.robot2.position.x, self.robot2.position.y))
            

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
            "couleur": self.robot.couleur ,
        }

   
  