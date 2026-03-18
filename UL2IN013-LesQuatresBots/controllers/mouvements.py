"""Mouvements programmes pour le robot"""
import time


def carre(robot, cote: float, delay: float = 0.1, verbose: bool = True):
    """Fait faire un carre au robot"""
    segment = cote / 10

    for i in range(4):
        robot.tourner(90)
        if verbose:
            print(f"Cote n°{i+1} - Position: {robot.get_location()}")

        for _ in range(10):
            robot.avancer(segment, delay)
            if verbose:
                x, y, angle, vitesse = robot.get_location()
                print(f"  -> x={x:.1f}, y={y:.1f}, angle={angle}, v={vitesse:.2f}")
            time.sleep(delay)


def rectangle(robot, largeur: float, hauteur: float, delay: float = 0.1, verbose: bool = True):
    """Fait faire un rectangle au robot"""
    dimensions = [largeur, hauteur, largeur, hauteur]

    for i, distance in enumerate(dimensions):
        robot.tourner(90)
        if verbose:
            print(f"Cote {i+1} (dist={distance})")

        segment = distance / 10
        for _ in range(10):
            robot.avancer(segment, delay)
            time.sleep(delay)


def triangle_equilateral(robot, cote: float, delay: float = 0.1, verbose: bool = True):
    """Fait faire un triangle au robot"""
    segment = cote / 10

    for i in range(3):
        robot.tourner(120)  # 360/3
        if verbose:
            print(f"Cote n°{i+1}")

        for _ in range(10):
            robot.avancer(segment, delay)
            time.sleep(delay)


def cercle(robot, rayon: float, nb_segments: int = 36, delay: float = 0.05, verbose: bool = False):
    """Fait faire un cercle au robot"""
    angle = 360 / nb_segments
    circonference = 2 * 3.14159 * rayon
    segment = circonference / nb_segments

    for i in range(nb_segments):
        robot.tourner(int(angle))
        robot.avancer(segment, delay)
        if verbose:
            print(f"Segment {i+1}/{nb_segments}")
        time.sleep(delay)


def aller_retour(robot, distance: float, delay: float = 0.1, verbose: bool = True):
    """Fait faire un aller-retour au robot"""
    segment = distance / 10

    if verbose:
        print("Aller")
    for _ in range(10):
        robot.avancer(segment, delay)
        time.sleep(delay)

    robot.tourner(180)

    if verbose:
        print("Retour")
    for _ in range(10):
        robot.avancer(segment, delay)
        time.sleep(delay)

    robot.tourner(180)
