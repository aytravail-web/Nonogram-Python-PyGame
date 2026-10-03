# coding=utf-8
# Model/Cellule.py
#
from pygame.color import Color

from Model.Bloc import COULEUR
from Model.debug import debug
from Model.CustomTypes import Cellule

# Clé contenant la valeur d'une cellule
VALEUR = "value"


#
# La Cellule
#
# L'objet cellule va représenter une case de l'image (du nonogram)
#
# La cellule sera représentée par un dictionnaire.
# Une cellule pourra être :
#   - vide (absence de bille) : La valeur sera 0.
#   - non découverte (non connue) : la valeur sera None.
#   - une couleur (ou plutôt l'indice non nul d'une couleur, la palette sera fournie plus tard).
#


def type_cellule(cell: Cellule) -> bool:
    """
    Permet de vérifier si l'argument peut correspondre ou non à une cellule

    :param cell: Objet dont on veut tester le type
    :return: True s'il s'agit d'une cellule, False sinon.
    """
    if type(cell) is not dict:
        debug(f"La cellule {cell} n'est pas un dictionnaire")
        return False
    if VALEUR not in cell:
        debug(f"La clé VALUE ({VALEUR}) n'est pas dans le dictionnaire")
        return False
    if cell[VALEUR] is not None and type(cell[VALEUR]) is not int:
        debug(f"La valeur {cell[VALEUR]} n'est ni entière ni None ")
        return False
    return True


#=============== DEBUT DU CODE ===================================

def construireCellule() -> Cellule:
    """
    Crée un dictionnaire représentant une cellule vide.
    :return: Un dictionnaire contenant l'unique clé VALEUR associée à None.
    """
    return {VALEUR: None}


def isVuCellule(cellule:Cellule)-> bool:
    """
    Vérifie si la cellule est découverte (si sa valeur est différente de None).

    :param cellule: Le dictionnaire représentant la cellule à tester.
    :return: True si la cellule est découverte, False sinon.
    """
    assert type_cellule(cellule), f"isVuCellule : Le paramètre {cellule} n'est pas une cellule."
    res = False
    if cellule[VALEUR] is not None:
        res = True
    return res


def isVideCellule(cellule:Cellule)->bool:
    """
    Vérifie si la cellule est vide (si sa valeur est égal à 0).
    :param cellule:Le dictionnaire représentant la cellule à tester.
    :return: True si la cellule est vide, False sinon.
    """
    assert type_cellule(cellule), f"isVideCellule : Le paramètre {cellule} n'est pas une cellule."
    res = False
    if cellule[VALEUR] == 0 :
        res = True
    return res


def getCouleurCellule(cellule:Cellule)->int:
    """
    Donne la couleur de la cellule.
    :param cellule: Le dictionnaire représentant la cellule à tester.
    :return: Retourne la couleur de la cellule.

    """
    assert type_cellule(cellule), f"getCouleurCellule : Le paramètre {cellule} n'est pas une cellule."
    assert cellule[VALEUR] is not None , f"getCouleurCellule : la cellule ne contient pas de couleur.."

    return cellule[VALEUR]


def setCouleurCellule(cellule : Cellule,nb_couleur:int)->None:
    """
    Modifie la couleur de la cellule.
    :param cellule: Le dictionnaire représentant la cellule à tester.
    :param nb_couleur: L'entier qui donnera la nouvelle couleur de la Cellule
    :return: Rien
    """
    assert type_cellule(cellule), f"setCouleurCellule : Le paramètre {cellule} n'est pas une cellule."
    assert type(nb_couleur) is int, f"setCouleurCellule : Le paramètre n'est pas un entier."

    cellule[VALEUR] = nb_couleur

    return None


def setNonVuCellule(cellule : Cellule)->None:
    """
    attribut None a la cellule, pour la transformée en cellule Non vu.
    :param cellule: Le dictionnaire représentant la cellule à tester.
    :return: Rien
    """
    assert type_cellule(cellule), f"setNonVuCellule : Le paramètre {cellule} n'est pas une cellule."

    cellule[VALEUR] = None

    return None