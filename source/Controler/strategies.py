# Mouvements.py : mouvements programmés pour le robot
from Model.vecteur import Vecteur

class Stop:
    def executer(self, robot):
        while abs(robot.v_rg) > 0 or abs(robot.v_rd) > 0:
            if robot.v_rg > 0:
                robot.v_roue("g", -1)
            elif robot.v_rg < 0:
                robot.v_roue("g", 1)

            if robot.v_rd > 0:
                robot.v_roue("d", -1)
            elif robot.v_rd < 0:
                robot.v_roue("d", 1)

            yield

class Avancer:
    def __init__(self, distance):
        self.distance = distance

    def executer(self, robot):
        dep_x, dep_y = robot.get_location()

        while True:
            dist_parc = Vecteur(robot.x - dep_x, robot.y - dep_y).norme()
            restant = min(self.distance - dist_parc, robot.dist_obs - 5)

            if restant <= 0:
                break

            d_stop = robot.v_rg ** 2 / (2 * robot.accel)

            if d_stop < restant - robot.v_rg:
                robot.v_roue("g", 1)
                robot.v_roue("d", 1)
            else:
                robot.v_roue("g", -1)
                robot.v_roue("d", -1)

            yield

        yield from Stop().executer(robot)
    

class Tourner:
    def __init__(self, angle):
        self.angle = angle

    def executer(self, robot):
        angle_restant = self.angle
        last_rot = robot.rotation

        while abs(angle_restant) > 0.5:
            omega = (robot.rotation - last_rot + 180) % 360 - 180
            last_rot = robot.rotation
            angle_restant -= omega

            theta_stop = omega ** 2 / (2 * robot.accel)

            if abs(angle_restant) <= theta_stop + abs(omega):
                if angle_restant > 0:
                    robot.v_roue("g", 1)
                    robot.v_roue("d", -1)
                else:
                    robot.v_roue("g", -1)
                    robot.v_roue("d", 1)
            else:
                if angle_restant > 0:
                    robot.v_roue("g", -1)
                    robot.v_roue("d", 1)
                else:
                    robot.v_roue("g", 1)
                    robot.v_roue("d", -1)

            yield

        yield from Stop().executer(robot)


class Carre:
    def __init__(self, cote):
        self.cote = cote

    def executer(self, robot):
        for _ in range(4):
            yield from Avancer(self.cote).executer(robot)
            yield from Tourner(90).executer(robot)

