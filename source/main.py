# main.py : initialise la simulation/le controleur du robot
# NB: le code ne devrait pas depasser une dizaine de lignes, il doit juste appeler les autres modules (voir exemple du cours4)

from controleur.step import Step
from controleur.strategies import StrategieCarre
from model.arene import Arene
from model.robot import Robot
from view2d.affichage import Affichage

def main():
    arene = Arene()
    robot = Robot()
    strategie = StrategieCarre(100)
    step = Step(robot, arene, strategie)
    vue = Affichage(arene, robot, step)
    vue.lancer_simulation()

if __name__ == "__main__":
    main()
