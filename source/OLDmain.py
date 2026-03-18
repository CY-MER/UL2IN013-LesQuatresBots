# main.py : programme principal reliant les autres entre eux
import pygame
from Model.robot import Robot
from Model.obstacle import Polygone
from Controler.strategies import Avancer, Tourner, Carre
from Model.vecteur import Vecteur
from View_2D.affichage import Affichage

""" Constantes """
TPS = 60

"""Initialisation de la simulation"""
clock = pygame.time.Clock()

""" Objets """
robot = Robot() # creation du robot
mur = Polygone([Vecteur(220, -300), Vecteur(240, 320), Vecteur(160, -300)]) # creation d'un mur
toit = Polygone([Vecteur(300, 300), Vecteur(-300, 240), Vecteur(-300, 100)]) # creation d'un toit
obstacles = [mur, toit] # liste des polygones
liste_mv = [Tourner(380), Carre(300)] # liste des strategies appelés dans l'ordre
affichage = Affichage(robot, obstacles) # sortie graphique


def update_robot(robot, obstacles, liste_mv):
    """Met à jour le robot et exécute les mouvements"""

    instruc = 0
    robot.raycast(obstacles)
    robot.update()

    try:
        next(liste_mv[instruc].executer(robot))
    except StopIteration:
        if instruc + 1 < len(liste_mv):
            instruc += 1
    return

def mainLoop():
    execution = True # fenetre en cours d'execution
    while execution:
            """ Gestion des evenements """
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # fermeture de la fenetre
                    execution = False

            """ Mise à jour de la position/rotation du robot (modifie les attributs du robot) """
            update_robot(robot, obstacles, liste_mv)
            affichage.updateAffichage()
            clock.tick(TPS)
    pygame.quit()

if __name__ == "__main__":
    mainLoop()

