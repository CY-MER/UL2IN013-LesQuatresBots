# Mouvements.py : mouvements programmés pour le robot
import time

def carre(robot, cote:float, delay:float=0.1):
    """ fait faire un carré au robot
    - cote: longueur des cotés du carré
    - delay: temps entre chaque étape (pour le suivi)
    """
    for i in range(4):
        robot.tourner(90)
        print(robot.get_location()) # suivit du robot

        print("Coté n°", i+1)
        for _ in range(10):
            robot.avancer(cote/10, delay)
            print(robot.get_location()) # suivit du robot
            time.sleep(delay)
