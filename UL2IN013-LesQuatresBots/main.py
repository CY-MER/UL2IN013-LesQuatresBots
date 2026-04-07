"""Programme principal"""
from controllers import GameController


def main():
    controller = GameController(width=400, height=400)
    controller.run()


if __name__ == "__main__":
    main()

