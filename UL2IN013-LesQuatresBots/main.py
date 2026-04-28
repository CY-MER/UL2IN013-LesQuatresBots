"""Programme principal"""
from controllers import GameController
from controllers.strategie import Avancer, StratSequence, Tourner
from api.robot2I013 import Robot2IN013
from api.robotadapter import RobotAdapter


def main_simulation():
    """Lance la simulation pygame"""
    controller = GameController(width=400, height=400)
    controller.run()


def main_reel():
    """Lance le vrai robot GoPiGo via SSH sur Raspberry Pi"""
    robot_physique = Robot2IN013()
    robot = RobotAdapter(robot_physique)
    strategie = StratSequence([
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
            Avancer(100),
            Tourner(90),
        ])  # carré 

    print("Démarrage robot réel...")
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


if __name__ == "__main__":
    #main_simulation()   
     main_reel()       