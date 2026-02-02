import pygame
from robot import Robot
from mouvements import carre

pygame.init()
SCREEN_SIZE = 500
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Robot trace un carré")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

robot = Robot(x=SCREEN_SIZE/2, y=SCREEN_SIZE/2, rot=0)
points = [(robot.x, robot.y)]

def carre_graphique(robot, cote: float, steps: int = 10, delay: float = 0.1):
    for i in range(4):
        robot.tourner(90)
        points.append((robot.x, robot.y))
        for step in range(steps):
            robot.avancer(cote / steps, delay)
            points.append((robot.x, robot.y))

            screen.fill(WHITE)
            if len(points) > 1:
                pygame.draw.lines(screen, RED, False, [(int(p[0]), int(p[1])) for p in points], 2)
            pygame.draw.circle(screen, BLACK, (int(robot.x), int(robot.y)), 5)

            pygame.display.flip()
            clock.tick(60)
            pygame.event.pump()

running = True
started = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not started:
        carre_graphique(robot, cote=100, steps=20, delay=0.05)
        started = True

pygame.quit()
