# affichage.py : gère l'affichage de la simulation en 2D avec Pygame
import pygame
from Model.robot import Robot
from Model.vecteur import Vecteur

""" Constantes """
LARGEUR, HAUTEUR = 1200, 700 # taille de la fenetre en pixels
FPS = 60 # images par seconde (augmenter cette valeur rend l'animation plus fluide mais l'accelere)

def convertion(x:float, y:float, screen):
    """ Convertit les coordonées arbitraire en pixels sur l'écran, point(0,0) est le centre de l'écran """
    cx = screen.get_width() // 2 + int(x)
    cy = screen.get_height() // 2 - int(y) # y inversé car l'origine est en haut a gauche
    return cx, cy

def dessine_polygone(polygone, screen, color=(0, 255, 0)):
    """ Fonction pour dessiner un polygone quelconque sur l'écran """
    points = [convertion(p.x, p.y, screen) for p in polygone.get_points()]
    pygame.draw.polygon(screen, color, points)

def dessine_robot(robot:Robot, screen):
    """ Fonction pour dessiner le robot sur l'écran """
    dessine_polygone(robot.get_forme(), screen, color=(0, 100, 255)) # dessine le robot (rectangle bleu)
    # capteur du robot (ligne rouge)
    tete_x, tete_y = robot.get_location_tete()
    tx, ty = convertion(tete_x, tete_y, screen)
    cible_x, cible_y = robot.get_cible_capteur()
    cx, cy = convertion(cible_x, cible_y, screen)
    pygame.draw.line(screen, (255, 0, 0), (tx, ty), (cx, cy), 1)

class Affichage:
    def __init__(self, robot, obstacles:list):
        """ Initialisation des objets """
        self.robot = robot
        self.obstacles = obstacles

        """ Initialisation de Pygame """
        pygame.init()
        self.screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Simulation robot")
        self.clock = pygame.time.Clock()

    def updateAffichage(self):
        """Affichage graphique"""
        self.screen.fill((220, 220, 220))

        for obs in self.obstacles:
            dessine_polygone(obs, self.screen, color=(100, 100, 55))

        dessine_robot(self.robot, self.screen)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Distance libre: {self.robot.dist_obs}", True, (0, 0, 0))
        text2 = font.render(
            f"Vitesse roue gauche: {self.robot.v_rg}, roue droite: {self.robot.v_rd}",
            True, (0, 0, 0)
        )
        self.screen.blit(text, (10, 10))
        self.screen.blit(text2, (10, 50))
    
        if self.robot.cible_obs is not None:
            px = convertion(self.robot.cible_obs[0].x, self.robot.cible_obs[0].y, self.screen)
            py = convertion(self.robot.cible_obs[1].x, self.robot.cible_obs[1].y, self.screen)
            pygame.draw.line(self.screen, (0, 255, 0), px, py, 10)

        pygame.display.flip()


    def run(self):
        execution = True # fenetre en cours d'execution
        while execution:
                """ Gestion des evenements """
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # fermeture de la fenetre
                        execution = False

                self.updateAffichage()
                self.clock.tick(FPS)
        pygame.quit()

