from models import Robot 
from models.obstacle import Obstacle
from .strategie import  StratSequence,Avancer,Tourner,Stop 
class SimulationController: 
    """gère uniquement l'etat et l'evolution de la simulation"""

    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """Réinitialise la simulation"""
        self.robot = Robot(0 , 350) # position de départ du robot
        self.dessin = False # dessine le chemin du robot ou pas
        self.points = [(self.robot.position.x, self.robot.position.y)]
        self.robot.dessine_trace(False) # active ou désactive le dessin
        self.path = []
        self.robot_set_couleur = (255, 255, 0) # jaune
        
        self.obstacles = [
            Obstacle("cercle", (200, 200, 30), couleur=(255,0,0)),# rouge
            Obstacle("rectangle",(180, 10, 60, 30), couleur=(0,255,0)),# vert
            Obstacle("rectangle", (180, 350, 60,30), couleur=(0,0,255)),# bleu
        ]

        #self.strategie = Carre(100)
        self.strategie = StratSequence([
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
        ])
        
    def update(self):
        """Met à jour la simulation"""
        old_x, old_y = self.robot.position.x, self.robot.position.y

        self.strategie.update(self.robot) # update les strategie 
        self.robot.update() # update la position du robot 

        for obstacle in self.obstacles: # gere les obstacle (monde)
            if obstacle.collision(self.robot):
                self.robot.position.x = old_x
                self.robot.position.y = old_y
                self.robot.stop()
                self.strategie = Stop()
                print("Collision !")
                
                return 
        
        self.points.append((self.robot.position.x, self.robot.position.y))
            

    def get_robot_info(self):
        """Retourne les infos utiles pour l'affichage"""
        x, y, angle, vitesse = self.robot.get_location()
        return {
            "x": x,
            "y": y,
            "angle": angle,
            "vitesse": vitesse,
            "points": self.points,
            "path": self.robot.path,
            "couleur" : self.robot.couleur,
            "obstacles": self.obstacles,
            "couleur" : self.robot.couleur
        }
