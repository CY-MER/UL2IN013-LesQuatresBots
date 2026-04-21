"""Programme principal"""
from api.robot2in013 import Robot2IN013
from api.robot_adapter import RobotAdapter
from controllers import GameController
from controllers.strategie import Carre
#from easygopigo3 import EasyGoPiGo3,Servo,DistanceSensor,MotionSensor 
def main_simulation():
    """Lance la simulation pygame"""
    controller = GameController(width=400, height=400)
    controller.run()


def main_real():
    """Lance le vrai robot"""
    robot_phy = Robot2IN013()
    robot = RobotAdapter(robot_phy)
    strategie = Carre(100)

    print("Démarrage du robot réel...")
    print("Ctrl+C pour arrêter")

    try:
        while not strategie.fini():
            strategie.update(robot)
            robot.update()

    except KeyboardInterrupt:
        print("Arrêt demandé")

    finally:
        robot.stop()
        print("Robot arrêté")


if __name__ == "__main_real__":
    main_real()       # vrai robot
    #main_simulation()  # simulation