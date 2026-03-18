"""Demo des mouvements"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Robot
from controllers import carre, rectangle, triangle_equilateral, cercle, aller_retour


def demo_carre():
    print("\n=== CARRE ===")
    robot = Robot(0, 0, 0)
    carre(robot, cote=40, delay=0.05, verbose=True)
    print(f"Final: {robot}")


def demo_rectangle():
    print("\n=== RECTANGLE ===")
    robot = Robot(0, 0, 0)
    rectangle(robot, largeur=50, hauteur=30, delay=0.05, verbose=True)
    print(f"Final: {robot}")


def demo_triangle():
    print("\n=== TRIANGLE ===")
    robot = Robot(0, 0, 0)
    triangle_equilateral(robot, cote=40, delay=0.05, verbose=True)
    print(f"Final: {robot}")


def demo_cercle():
    print("\n=== CERCLE ===")
    robot = Robot(0, 0, 0)
    cercle(robot, rayon=20, nb_segments=36, delay=0.02, verbose=False)
    print(f"Final: {robot}")


def demo_aller_retour():
    print("\n=== ALLER-RETOUR ===")
    robot = Robot(0, 0, 0)
    aller_retour(robot, distance=50, delay=0.05, verbose=True)
    print(f"Final: {robot}")


def main():
    print("\nDemo Mouvements Robot")
    print("1. Carre")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Cercle")
    print("5. Aller-Retour")
    print("0. Tout")

    demos = {
        "1": demo_carre,
        "2": demo_rectangle,
        "3": demo_triangle,
        "4": demo_cercle,
        "5": demo_aller_retour
    }

    try:
        choice = input("\nChoix (0-5): ").strip()

        if choice == "0":
            for demo in demos.values():
                demo()
        elif choice in demos:
            demos[choice]()
        else:
            print("Invalide")

    except KeyboardInterrupt:
        print("\nInterrompu")


if __name__ == "__main__":
    main()
