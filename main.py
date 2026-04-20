"""Programme principal"""
from controllers import GameController
from API import Robot2IN013

def main():
    robot = Robot2IN013()
    controller = GameController(width=400, height=400)
    controller.run()


if __name__ == "__main__":
    main()
