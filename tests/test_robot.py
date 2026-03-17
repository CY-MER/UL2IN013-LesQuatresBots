"""Tests robot"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Robot
from controllers import carre, rectangle, aller_retour
import math


def test_initialisation():
    robot = Robot()
    x, y, angle, vitesse = robot.get_location()

    assert x == 0.0, "x incorrect"
    assert y == 0.0, "y incorrect"
    assert angle == 0, "angle incorrect"
    assert vitesse == 0.0, "vitesse incorrecte"
    print("[OK] initialisation")


def test_avancer():
    robot = Robot(0, 0, 0)
    robot.avancer(10, dt=2)
    x, y, angle, vitesse = robot.get_location()

    assert x == 10.0, "x incorrect"
    assert y == 0.0, "y incorrect"
    assert vitesse == 5.0, "vitesse incorrecte"
    print("[OK] avancer")


def test_reculer():
    robot = Robot(10, 0, 0)
    robot.reculer(5, dt=1)
    x, y, _, _ = robot.get_location()

    assert math.isclose(x, 5.0, abs_tol=0.01), "x incorrect"
    assert math.isclose(y, 0.0, abs_tol=0.01), "y incorrect"
    print("[OK] reculer")


def test_tourner():
    robot = Robot()
    robot.tourner(90)
    assert robot.rotation == 90, "90 deg incorrect"

    robot.tourner(300)
    assert robot.rotation == 30, "modulo incorrect"
    print("[OK] tourner")


def test_tourner_tete():
    robot = Robot(0, 0, 0, rot_tete=0)
    robot.tourner_tete(45)
    assert robot.rotation_tete == 45, "tete incorrect"

    robot.tourner_tete(320)
    assert robot.rotation_tete == 5, "modulo tete incorrect"
    print("[OK] tourner_tete")


def test_capteur():
    robot = Robot(0, 0, 0, sens=10)
    cx, cy = robot.get_cible_capteur()

    assert cx == 10.0, "cx incorrect"
    assert cy == 0.0, "cy incorrect"

    robot.tourner(90)
    cx, cy = robot.get_cible_capteur()

    assert math.isclose(cx, 0.0, abs_tol=0.01), "cx rotation incorrect"
    assert math.isclose(cy, 10.0, abs_tol=0.01), "cy rotation incorrect"
    print("[OK] capteur")


def test_carre():
    print("\n--- test carre ---")
    robot = Robot(0, 0, 0)
    carre(robot, 20, delay=0.01, verbose=False)

    x, y, angle, _ = robot.get_location()
    assert math.isclose(x, 0.0, abs_tol=0.01), f"x final {x}"
    assert math.isclose(y, 0.0, abs_tol=0.01), f"y final {y}"
    assert angle == 0, f"angle final {angle}"
    print("[OK] carre")


def test_rectangle():
    robot = Robot(0, 0, 0)
    rectangle(robot, largeur=20, hauteur=10, delay=0.01, verbose=False)

    x, y, angle, _ = robot.get_location()
    assert math.isclose(x, 0.0, abs_tol=0.1), f"x {x}"
    assert math.isclose(y, 0.0, abs_tol=0.1), f"y {y}"
    print("[OK] rectangle")


def test_aller_retour():
    robot = Robot(0, 0, 0)
    aller_retour(robot, distance=20, delay=0.01, verbose=False)

    x, y, angle, _ = robot.get_location()
    assert math.isclose(x, 0.0, abs_tol=0.1), f"x {x}"
    assert math.isclose(y, 0.0, abs_tol=0.1), f"y {y}"
    assert angle == 0, f"angle {angle}"
    print("[OK] aller_retour")


def test_repr():
    robot = Robot(10, 20, 90)
    repr_str = repr(robot)
    assert "10.00" in repr_str
    assert "20.00" in repr_str
    assert "90" in repr_str
    print("[OK] repr")


def main():
    print("Tests Robot")

    tests = [
        test_initialisation,
        test_avancer,
        test_reculer,
        test_tourner,
        test_tourner_tete,
        test_capteur,
        test_carre,
        test_rectangle,
        test_aller_retour,
        test_repr
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1

    print(f"\nResultat: {passed} OK, {failed} FAIL")
    if failed == 0:
        print("Tous les tests passent")


if __name__ == "__main__":
    main()
