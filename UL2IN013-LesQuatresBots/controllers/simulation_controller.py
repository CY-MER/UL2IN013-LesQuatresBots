from models import Robot 
from models.obstacle import Obstacle 
from .strategie import StratSequence, Stop , Avancer , Tourner  

class SimulationController: 
    """gère uniquement l'etat et l'evolution de la simulation"""

    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """Réinitialise la simulation"""
        self.robot = Robot (65, self.height - 65 )
        self.robot.dessine_trace(True)
        self.robot.set_couleur((0,255,0)) #vert 

        self.robot1 = Robot(self.width - 65, self.height - 65)
        self.robot1.dessine_trace(True)
        self.robot1.set_couleur((255,0,0)) #rouge 

        self.robots = [self.robot, self.robot1]

        self.points = [(self.robot.position.x, self.robot.position.y)]


        self.obstacles = [
            Obstacle("rectangle", (100, 100, 60, 30), couleur=(255,0,0)),# rouge
            Obstacle("rectangle",(100, 200, 60, 30), couleur=(0,255,0)),# vert
            Obstacle("rectangle", (100, 300, 60,30), couleur=(0,0,255)),# bleu
        ]

        self.strategies = [StratSequence([
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
        ]),

        StratSequence([
            Avancer(150),
            Tourner (180),
            Avancer (150),
            Tourner(180),
        ])]


    def update(self):
        """Met à jour la simulation"""
        for i, robot in enumerate(self.robots):

            old_x, old_y = robot.position.x, robot.position.y

            self.strategies[i].update(robot)
            robot.update()

            for obstacle in self.obstacles:
                if obstacle.collision(robot):
                    robot.position.x = old_x
                    robot.position.y = old_y
                    robot.stop()
                    self.strategies[i] = Stop()
                    print("Collision !")
                    return
        
        self.points.append((self.robot.position.x, self.robot.position.y))
        
            

    def get_robots_info(self):
        """Retourne les infos utiles pour l'affichage"""

        robots =[]
        for robot in self.robots :
            x, y, angle, vitesse , path , couleur = robot.get_location()
            robots.append({
                "x": x,
                "y": y,
                "angle": angle,
                "vitesse": vitesse,
                "path": path,
                "couleur" : couleur
            })
        return {
            "robots": robots,
            "obstacles": self.obstacles

            }
