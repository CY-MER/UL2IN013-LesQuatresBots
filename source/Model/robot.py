# robot.py : classe pour simuler le robot et ses caractéristiques
import math
from Model.obstacle import Polygone
from Model.vecteur import Vecteur
from Model.arene import collision_points

class Robot:
    def __init__(self, x:float=0, y:float=0, capt:int=200):
        """ Initialisation du robot"""
        self.x = x
        self.y = y
        self.rotation = 0 # rotation du corps du robot
        self.rotation_tete = 0 # rotation de la tete par rapport au corps
        self.longeur = 40 # longueur du corps du robot
        
        self.v_rg = 0 # vitesse de rotation de la roue gauche
        self.v_rd = 0 # vitesse de rotation de la roue droite
        self.v_max = 5 # vitesse maximale du robot
        self.accel = 0.1 # acceleration du robot (vitesse augmente de cette valeur par frame)

        self.portee_capteur = capt # portee du capteur
        self.dist_obs = capt # distance libre devant le robot
        self.cible_obs = None # position de l'obstacle (sous forme de segment)

    def avancer_discret(self, dist:float):
        """ fait avancer le robot dans la direction de sa rotation """
        vec = Vecteur(dist, 0).rotation(self.rotation)
        self.x += vec.x
        self.y += vec.y

    def tourner_discret(self, a:int):
        """ fait tourner le robot d'un angle a """
        self.rotation = (self.rotation + a) % 360

    def v_roue(self, roue:str, scal:int):
        """ accelere ou decelere une roue du robot, roue:[g,d], scal:[-1,1] """
        if roue == "g":
            self.v_rg = max(min(round(self.v_rg + scal * self.accel, 2), self.v_max), -self.v_max) # ne depasse pas v_max dans les deux sens
        elif roue == "d":
            self.v_rd = max(min(round(self.v_rd + scal * self.accel, 2), self.v_max), -self.v_max) # idem
    
    def update(self):
        """ met a jour la position et la rotation du robot en fonction de la vitesse de ses roues (a appeler a chaque frame) """
        if self.v_rg == self.v_rd: # les deux roues ont la même vitesse -> ligne droite
            self.avancer_discret(self.v_rg)
        else: # les roues ont des vitesses différentes -> rotation
            R = self.longeur/2 * (self.v_rg + self.v_rd) / (self.v_rd - self.v_rg) # rayon de courbure du robot
            omega = (self.v_rd - self.v_rg) / self.longeur # vitesse angulaire du robot
            self.rotation = (self.rotation + math.degrees(omega)) % 360 # mise à jour de la rotation du robot
            vec = Vecteur(R, 0).rotation(self.rotation) # vecteur du centre de rotation
            self.x += vec.x
            self.y += vec.y

    def get_location(self):
        """ renvoie la position et l'orientation du robot """
        return self.x, self.y
    
    def get_rot_totale(self):
        """ renvoie la rotation totale du capteur (rotation du corps + rotation de la tete) """
        return (self.rotation + self.rotation_tete) % 360
    
    def get_location_tete(self):
        """ renvoie la position et l'orientation de la tete du robot """
        vect = Vecteur(self.longeur/2, 0).rotation(self.rotation)
        x_tete = self.x + vect.x
        y_tete = self.y + vect.y
        return x_tete, y_tete

    def get_cible_capteur(self):
        """ renvoie la position regardée par le capteur en fonction de la rotation du robot et celle de sa tete """
        vect = Vecteur(self.portee_capteur + self.longeur/2, 0).rotation(self.get_rot_totale())
        cible_x = self.x + vect.x
        cible_y = self.y + vect.y
        return cible_x, cible_y

    def get_forme(self)->Polygone:
        """ renvoie le quadrilatère représentant la hitbox du robot en fonction de sa position et de sa rotation """
        # points du robot avant rotation et translation (centrés sur l'origine)
        vecteurs = [Vecteur(-self.longeur/2, -15), Vecteur(self.longeur/2, -11), Vecteur(self.longeur/2, 11), Vecteur(-self.longeur/2, 15)]
        points = [] # points calculés
        for vec in vecteurs:
            vec_rot = vec.rotation(self.rotation) # rotation du segment
            points.append(Vecteur(vec_rot.x + self.x, vec_rot.y + self.y))
        return Polygone(points)
    
    def raycast(self, obstacles:list, ray_size:float=5):
        """ renvoie la distance entre le robot et l'obstacle le plus proche dans la direction du capteur """
        ray_vec = Vecteur(ray_size, 0).rotation(self.get_rot_totale()) # vecteur du raycast dans la direction du capteur
        tete_x, tete_y = self.get_location_tete()
        ray_x = Vecteur(tete_x, tete_y) # depart du segment raycast
        ray_y = Vecteur(tete_x + ray_vec.x, tete_y + ray_vec.y) # arrivee du segment raycast

        for ray_i in range(int(self.portee_capteur/ray_size)): # couper la portee en rayons de taille ray_size
            for poly in obstacles:
                points = poly.get_points()
                for j in range(len(points)):
                    if collision_points(ray_x, ray_y, points[j], points[(j+1) % len(points)]):
                        self.dist_obs = ray_i * ray_size # nombre de rayons avant collision * taille du rayon
                        self.cible_obs = (Vecteur(ray_x.x, ray_x.y), Vecteur(ray_y.x, ray_y.y))
                        return # collision
            ray_x.x += ray_vec.x - 0.01 # ajout d'un epsilon pour eviter de rater la collision
            ray_x.y += ray_vec.y - 0.01
            ray_y.x += ray_vec.x - 0.01
            ray_y.y += ray_vec.y - 0.01
        self.dist_obs = self.portee_capteur
        self.cible_obs = None
        return # pas de collision après max rayons
