from robot import Robot 
from mouvement import carre 
import math 


def test_initialisation():
    robot = Robot()
    x, y, angle, vitesse = robot.get_location()

    assert x == 0.0, "x initial incorrect"
    assert y == 0.0, "y initial incorrect"
    assert angle == 0, "rotation initiale incorrecte"
    assert vitesse == 0.0, "vitesse initiale incorrecte"
    print(" Test initialisation OK")

def test_avancer():
    robot = Robot(0, 0, 0)
    robot.avancer(10, dt=2)

    x, y, angle, vitesse = robot.get_location()

    assert x == 10.0, "avancer() : x incorrect"
    assert y == 0.0, "avancer() : y incorrect"
    assert vitesse == 5.0, "avancer() : vitesse incorrecte"
    print("Test avancer OK") 

def test_tourner():
    robot = Robot()
    robot.tourner(90)
    assert robot.rotation == 90, "tourner() à 90° incorrect"

    robot.tourner(300)
    assert robot.rotation == 30, "tourner() modulo 360 incorrect"
    print(" Test tourner OK")

def test_capteur():
    robot = Robot(0, 0, 0, sens=10)
    cx, cy = robot.get_cible_capteur()

    assert cx == 10.0, "capteur x incorrect"
    assert cy == 0.0, "capteur y incorrect"

    robot.tourner(90)
    cx, cy = robot.get_cible_capteur()

    assert cx == 0.0, "capteur x après rotation incorrect"
    assert cy == 10.0, "capteur y après rotation incorrect"
    print(" Test capteur OK")


def test_carre():
    robot = Robot(0, 0, 0)
    carre(robot, 20, delay=0)

    x, y, angle, _ = robot.get_location()

    # le robot doit revenir à sa position de départ
    assert math.isclose(x, 0.0, abs_tol=0.01), "carré : x final incorrect"
    assert math.isclose(y, 0.0, abs_tol=0.01), "carré : y final incorrect"
    assert angle == 0, "carré : rotation finale incorrecte"
    print(" Test carré OK")
  
def main():
    print("=== DÉBUT DES TESTS ===")
    test_initialisation()
    test_avancer()
    test_tourner()
    test_capteur()
    test_carre()
    print("=== TOUS LES TESTS SONT VALIDES ✅ ===")


main()
