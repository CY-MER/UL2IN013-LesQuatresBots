# api/robot_adapter.py
import math
from api.robot2I013 import Robot2IN013


class RobotAdapter:
    """
    Traducteur entre les stratégies (Robot simulé) et le Robot2IN013 physique.
    Expose exactement la même interface que models/robot.py :
    - avancer(vitesse)
    - tourner(vitesse)
    - stop()
    - update(dt)
    - get_location()
    - position.x, position.y, rotation  ← lus par Avancer.fini() et Tourner.fini()
    """

    # Conversion vitesse simulation → degrés/sec
    # vitesse simulation = "pas par update", 1 pas ≈ 200 dps
    # À calibrer selon le comportement réel du robot
    SCALE = 400

    def __init__(self, robot_physique: Robot2IN013):
        self.robot = robot_physique

        # --- Position estimée (même interface que models/robot.py) ---
        self.position   = _Point(0.0, 0.0)
        self.rotation   = 0.0
        self.vitesse    = 0.0
        self.vitesse_rd = 0.0
        self.vitesse_rg = 0.0

        # --- Encodeurs au step précédent ---
        left, right = self.robot.get_motor_position()
        self._enc_left  = left
        self._enc_right = right

        # --- Constantes physiques (mm) ---
        self._wheel_circ  = Robot2IN013.WHEEL_CIRCUMFERENCE   # ≈ 208.9 mm
        self._wheel_base  = Robot2IN013.WHEEL_BASE_WIDTH       # = 117 mm

    # ------------------------------------------------------------------
    # Interface identique à models/robot.py
    # ------------------------------------------------------------------

    def avancer(self, vitesse: float):
        """Avance : les deux roues à la même vitesse"""
        self.vitesse_rd = vitesse
        self.vitesse_rg = vitesse
        dps = vitesse * self.SCALE
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)

    def tourner(self, vitesse: float):
        """Tourne : roues opposées"""
        self.vitesse_rd = -vitesse
        self.vitesse_rg =  vitesse
        dps = vitesse * self.SCALE
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,  -dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,  dps)

    def stop(self):
        """Arrête le robot"""
        self.vitesse_rd = 0.0
        self.vitesse_rg = 0.0
        self.vitesse    = 0.0
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, 0
        )

    def update(self, dt: float = 1.0):
        """
        Lit les encodeurs et recalcule position + rotation.
        Même rôle que Robot.update() dans la simulation.
        """
        # 1. Lire les encodeurs
        left, right = self.robot.get_motor_position()

        # 2. Delta depuis le dernier update (en degrés)
        delta_left  = left  - self._enc_left
        delta_right = right - self._enc_right
        self._enc_left  = left
        self._enc_right = right

        # 3. Convertir degrés → mm
        dist_left  = (delta_left  / 360.0) * self._wheel_circ
        dist_right = (delta_right / 360.0) * self._wheel_circ

        # 4. Distance moyenne = déplacement
        dist_moy = (dist_left + dist_right) / 2.0

        # 5. Changement d'angle (degrés)
        delta_angle = math.degrees(
            (dist_right - dist_left) / self._wheel_base
        )

        # 6. Mettre à jour rotation
        self.rotation = (self.rotation + delta_angle) % 360

        # 7. Mettre à jour position
        rad = math.radians(self.rotation)
        self.position.x += dist_moy * math.cos(rad)
        self.position.y += dist_moy * math.sin(rad)
        self.position.x  = round(self.position.x, 4)
        self.position.y  = round(self.position.y, 4)

        # 8. Vitesse estimée
        self.vitesse = dist_moy / dt if dt > 0 else 0.0

    def get_location(self):
        """Même interface que Robot.get_location()"""
        return (
            self.position.x,
            self.position.y,
            round(self.rotation, 4),
            round(self.vitesse, 4)
        )


# ------------------------------------------------------------------
# Classe utilitaire interne : reproduit models/point.py
# pour que position.x et position.y fonctionnent
# ------------------------------------------------------------------
class _Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y