import math

class RobotAdapter:
    """
    Traduit les commandes du Robot simulé vers le Robot2IN013 physique.
    Calcule la position et rotation réelles 
    """

    SCALE = 100  # facteur de conversion vitesse simulatio -< dps

    def __init__(self, robot_physique):
        self.robot = robot_physique

        # Position estimée du robot
        self.position_x = 0.0
        self.position_y = 0.0
        self.rotation = 0.0
        self.vitesse = 0.0

        # Mémoriser au step précédent
        left, right = self.robot.get_motor_position()
        self._last_left = left
        self._last_right = right

        # Constantes données du physiques du robot
        self.WHEEL_CIRCUMFERENCE = robot_physique.WHEEL_CIRCUMFERENCE  # mm
        self.WHEEL_BASE_WIDTH = robot_physique.WHEEL_BASE_WIDTH        # mm

    def avancer(self, vitesse: float):
        """Avance le robot : les deux roues à la même vitesse"""
        dps = vitesse * self.SCALE
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,
            dps
        )

    def tourner(self, vitesse: float):
        """Tourne le robot : roues opposées"""
        dps = vitesse * self.SCALE
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)

    def stop(self):
        """Arrête le robot"""
        self.robot.set_motor_dps(
            self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,
            0
        )
        self.vitesse = 0.0

    def update(self, dt=1.0):
        """
        Lit les encodeurs et met à jour position + rotation.
        À appeler à chaque step de la boucle principale.
        """
        #  Lire les encodeurs actuels
        left, right = self.robot.get_motor_position()

        #  Calculer la différence depuis le dernier update
        delta_left = left - self._last_left
        delta_right = right - self._last_right

        self._last_left = left
        self._last_right = right

        #  Convertir degrés à une  distance parcourue 
        # distance = (degrés / 360) * circonférence
        dist_left = (delta_left / 360.0) * self.WHEEL_CIRCUMFERENCE
        dist_right = (delta_right / 360.0) * self.WHEEL_CIRCUMFERENCE

        #  Distance moyenne = déplacement du robot
        dist_moy = (dist_left + dist_right) / 2.0

        #  Changement d'angle (en degrés)
        # si les roues vont à des vitesses différentes -> rotation
        delta_angle = math.degrees(
            (dist_right - dist_left) / self.WHEEL_BASE_WIDTH
        )

        #  Mettre à jour rotation
        self.rotation = (self.rotation + delta_angle) % 360

        #  Mettre à jour position XY
        rad = math.radians(self.rotation)
        self.position_x += dist_moy * math.cos(rad)
        self.position_y += dist_moy * math.sin(rad)

        #  Vitesse estimée
        self.vitesse = dist_moy / dt if dt > 0 else 0.0

    def get_location(self):
        """Retourne position et rotation estimées — même interface que Robot simulé"""
        return (
            round(self.position_x, 4),
            round(self.position_y, 4),
            round(self.rotation, 4),
            round(self.vitesse, 4)
        )