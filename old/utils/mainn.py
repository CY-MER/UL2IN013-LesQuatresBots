from obstacle import Obstacle     
from robot_vecteur import RobotVecteur  

# Création des obstacles
obstacles = [
    Obstacle("rectangle", (5, 5, 2, 2)),                 # rectangle
    Obstacle("cercle", (10, 10, 3)),                     # cercle
    Obstacle("triangle", ((15, 5), (17, 8), (19, 5)))    # triangle
]

# Création du robot-
robot = RobotVecteur(x=0, y=0, rot=0, taille=1, obstacles=obstacles)

# Déplacement et test des collisions
robot.avancer(6)  # avance de 6 unités
print("Position après 1er déplacement :", robot.get_location())

robot.tourner(45)  # tourne de 45 degrés
robot.avancer(10)  # avance encore
print("Position après 2ème déplacement :", robot.get_location())
