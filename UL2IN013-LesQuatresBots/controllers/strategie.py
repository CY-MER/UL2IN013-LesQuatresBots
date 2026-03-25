from models.vecteur2D import Vecteur2D
from models.robot_vecteur import RobotVecteur


class Stop:
    def executer(self,robot):
        termine = True 

        if robot.vitesse_rg>0:
            robot.vitesse("g",-1)
            termine= False
        elif robot.vitesse_rg<0:
            robot.vitesse("g",1)
            termine = False

        if robot.vitesse_rd>0:
            robot.vitesse("d",-1)
            termine= False
        elif robot.vitesse_rd<0:
            robot.vitesse("d",1)
            termine = False
        
        return termine 