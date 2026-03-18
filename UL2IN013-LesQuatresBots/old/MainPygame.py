import pygame
from robot import Robot  

#  Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))  # taille de la fenêtre
largeur, hauteur = screen.get_size() # récupère la taille de la fentre
pygame.display.set_caption("Robot ")      # titre de la fenêtre
clock = pygame.time.Clock()                    # pour contrôler la vitesse des frames
font = pygame.font.Font(None, 24)             # police pour afficher texte

#  Création du robot 
robot = Robot(200, 200)  
points = [(robot.x, robot.y)]  
cote = 100                    
steps = 40                     
side = 0                        
step = 0                        

en_pause_rotation = False

running = True
while running:
    #  fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tracer un carré 
    if side < 4:  # on trace 4 côtés
        if step == 0 and not en_pause_rotation:

            robot.tourner(90)     
            robot.vitesse = 0     # vitesse = 0 pendant la rotation
            en_pause_rotation = True 
        
        elif en_pause_rotation:
            en_pause_rotation = False
            step = 1   # on sort de la frame de pause
        
        elif step < steps:
            robot.avancer(cote/steps, dt=1) 
            robot.update(largeur, hauteur)
            points.append((robot.x, robot.y))  
            step += 1
        else:
            step = 0
            side += 1  

    #  Dessin
    screen.fill((255, 255, 255))  
    if len(points) > 1:
        # tracer la ligne rouge représentant le chemin
        pygame.draw.lines(screen, (255, 0, 0), False, [(int(p[0]), int(p[1])) for p in points], 2)
    # dessiner le robot comme un petit cercle noir
    pygame.draw.circle(screen, (0, 0, 0), (int(robot.x), int(robot.y)), 5)

    #  Affichage des informations du robot 
    x, y, angle, vitesse = robot.get_location()  
    screen.blit(font.render(f"x={x:.1f} y={y:.1f} angle={angle%360} vitesse={vitesse:.2f}", True, (0,0,0)), (10, 10))

    # Mettre à jour l'écran 
    pygame.display.flip()
    pygame.time.delay(100)  
    clock.tick(60)          

# Quitter Pygame
pygame.quit()
