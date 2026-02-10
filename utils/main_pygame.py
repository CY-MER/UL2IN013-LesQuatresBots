import pygame
from obstacle import Obstacle
from robot_vecteur import RobotVecteur
import math

# -------------------
# Initialisation Pygame
# -------------------
pygame.init()

LARGEUR, HAUTEUR = 800, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Test Robot + Obstacles")
clock = pygame.time.Clock()

# -------------------
# Couleurs
# -------------------
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# -------------------
# Création obstacles
# -------------------
obstacles = [
    Obstacle("rectangle", (100, 100, 150, 100)),
    Obstacle("cercle", (500, 300, 50)),
    Obstacle("triangle", ((600, 100), (700, 200), (650, 250)))
]

# -------------------
# Création robot
# -------------------
robot = RobotVecteur(x=50, y=50, rot=0)

# -------------------
# Boucle principale
# -------------------
running = True
while running:
    clock.tick(30)  # 30 FPS
    screen.fill(BLANC)

    # -------------------
    # Gestion des événements
    # -------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------
    # Contrôle du robot avec les touches
    # -------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        robot.avancer(5)
    if keys[pygame.K_DOWN]:
        robot.avancer(-5)
    if keys[pygame.K_LEFT]:
        robot.tourner(-5)
    if keys[pygame.K_RIGHT]:
        robot.tourner(5)

    # -------------------
    # Dessin obstacles
    # -------------------
    for obs in obstacles:
        if obs.type == "rectangle":
            x, y, w, h = obs.data
            pygame.draw.rect(screen, ROUGE, (x, y, w, h))
        elif obs.type == "cercle":
            cx, cy, r = obs.data
            pygame.draw.circle(screen, VERT, (int(cx), int(cy)), r)
        elif obs.type == "triangle":
            pygame.draw.polygon(screen, BLEU, obs.data)

    # -------------------
    # Dessin robot
    # -------------------
    x, y, rot, _ = robot.get_location()
    pygame.draw.circle(screen, NOIR, (int(x), int(y)), 10)  # robot comme un cercle de rayon 10
    # ligne direction
    dx = 15 * math.cos(math.radians(rot))
    dy = 15 * math.sin(math.radians(rot))
    pygame.draw.line(screen, NOIR, (int(x), int(y)), (int(x+dx), int(y+dy)), 2)

    # -------------------
    # Affichage
    # -------------------
    pygame.display.flip()

pygame.quit()
