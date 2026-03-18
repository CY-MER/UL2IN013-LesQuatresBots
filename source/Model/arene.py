# arene.py : initialise l'arène du robot
from Model.vecteur import Vecteur

def updateModel():
    """ Met a jour la simulation de l'arène """
    return

def collision_points(A: Vecteur, B: Vecteur, C: Vecteur, D: Vecteur)->bool:
        """ detecte une collision entre les segments AB et CD"""
        AB = A.point_vers_vecteur(B)
        AC = A.point_vers_vecteur(C)
        AD = A.point_vers_vecteur(D)
        CD = C.point_vers_vecteur(D)
        CA = C.point_vers_vecteur(A)
        CB = C.point_vers_vecteur(B)
        return AB.produit_vectoriel(AC) * AB.produit_vectoriel(AD) < 0 and CD.produit_vectoriel(CA) * CD.produit_vectoriel(CB) < 0