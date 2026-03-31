import pygame
import sys
import math
from models import RobotVecteur, Obstacle

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
FPS = 60
DISTANCE_CAPTEUR = 50  # Distance à laquelle le robot détecte l'obstacle

# --- COULEURS ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
GRAY  = (200, 200, 200)
class RobotFantome:
    """ Un robot invisible utilisé pour tester la collision en avance """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.y, 0, 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot Autonome avec Capteur")
    clock = pygame.time.Clock()

    # 1. Création du Robot (au centre)
    robot = RobotVecteur(400, 300, rot=0)

    # 2. Liste d'obstacles
    obstacles = [
        Obstacle("rectangle", (500, 100, 100, 200)),
        Obstacle("cercle", (200, 400, 60)),
        Obstacle("triangle", [(600, 400), (750, 500), (550, 550)])
    ]

    running = True
    vitesse_croisiere = 2

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- LOGIQUE DU CAPTEUR (ANTICIPATION) ---
        # On calcule où sera le robot s'il continue tout droit
        cible_x = robot.position.x + robot.direction.dx * DISTANCE_CAPTEUR
        cible_y = robot.position.y + robot.direction.dy * DISTANCE_CAPTEUR
        capteur = RobotFantome(cible_x, cible_y)

        # On vérifie si ce point futur touche un obstacle
        danger_imminent = False
        for obs in obstacles:
            if obs.collision(capteur):
                danger_imminent = True
                break

        # --- DÉCISION ---
        if danger_imminent:
            # S'il y a un danger, on s'arrête et on tourne sur place
            robot.vitesse = 0
            robot.tourner(2) # Il pivote doucement pour chercher une sortie
        else:
            # Sinon, on avance normalement
            robot.vitesse = vitesse_croisiere
            robot.avancer(robot.vitesse)

        # --- DESSIN ---
        # 1. Dessiner les obstacles
        for obs in obstacles:
            if obs.type == "rectangle":
                pygame.draw.rect(screen, BLACK, obs.data, 2)
            elif obs.type == "cercle":
                pygame.draw.circle(screen, BLACK, (obs.data[0], obs.data[1]), obs.data[2], 2)
            elif obs.type == "triangle":
                pygame.draw.polygon(screen, BLACK, obs.data, 2)

        # 2. Dessiner le capteur (la vision du robot)
        color_capteur = RED if danger_imminent else BLUE
        pygame.draw.line(screen, color_capteur, (robot.position.x, robot.position.y), (cible_x, cible_y), 1)
        pygame.draw.circle(screen, color_capteur, (int(cible_x), int(cible_y)), 3)

        # 3. Dessiner le robot
        robot_pos = (int(robot.position.x), int(robot.position.y))
        pygame.draw.circle(screen, GREEN, robot_pos, 10)

        # Gérer les bords de l'écran (rebond simple)
        if robot.position.x < 0 or robot.position.x > WIDTH or robot.position.y < 0 or robot.position.y > HEIGHT:
            robot.tourner(180)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
