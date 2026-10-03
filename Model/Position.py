# Model/Position.py
from Model.debug import *
from Model.CustomTypes import Position


#
# Les positions ne sont pas toujours faciles à gérer !
#
# Sur une image, quand on parle d'un pixel (x, y), x représente la colonne et y la ligne.
# Dans un tableau, quand on cherche la valeur tab[i][j], cette fois, c'est i qui désigne la ligne et j la colonne.
#
# Pour tenter d'éviter d'intervertir ligne/colonne, on va créer un dictionnaire avec deux clés bien explicites
# - la clé LIGNE qui représentera le numéro de ligne
# - la clé COLONNE qui représentera le numéro de colonne
#

LIGNE = "ligne"
COLONNE = "colonne"



def type_position(position: Position) -> bool:
    """
    Fonction permettant de déterminer si le paramètre peut représenter ou non une position.

    Cette fonction ne peut valider la valeur des lignes/colonnes

    :param position: Position à tester
    :return: True si le paramètre correspond à une position, False sinon
    """
    if type(position) is not dict:
        debug(f"Le paramètre {position} n'est pas un dictionnaire")
        return False
    if LIGNE not in position or COLONNE not in position:
        debug(f"Le dictionnaire {position} ne contient pas une des clés {LIGNE} ou {COLONNE}")
        return False
    if type(position[LIGNE]) is not int or type(position[COLONNE]) is not int:
        debug(f"Une des valeurs du dictionnaire {position} n'est pas un entier")
        return False
    return True


#============== DEBUT DU CODE ============================


def construirePosition()->Position:
    """
    Cette fonction se contente d’instancier un dictionnaire.
    :return:Un dictionnaire avec les deux clés LIGNE et COLONNE associées à la valeur 0, représentant ainsi la position (0, 0).
    """
    return {LIGNE: 0,COLONNE: 0}


def getLignePosition(dico:Position)->int:
    """
    Cette fonction reçoit un dictionnaire qui représenter une position
    :param dico: dictionnaire contenant les positions.
    :return:Retourne le numéro de ligne de cette position.
    """
    assert type_position(dico), f"getLignePosition : Les positions sont incorrect."

    return dico[LIGNE]

def getColonnePosition(dico:Position)->int:
    """
    Cette fonction reçoit un dictionnaire qui représenter une position
    :param dico: Dictionnaire contenant les positions.
    :return:Retourne le numéro de colonne de cette position.
    """
    assert type_position(dico), f"getColonnePosition : Les positions sont incorrect."

    return dico[COLONNE]


def setLignePosition(dico:Position,position_ligne:int)->None:
    """
    Cette fonction modifie la valeur de la ligne de la position avec l’entier passé en paramètre.
    :param dico: Dictionnaire contenant les positions.
    :param position_ligne: Valeur de la position remplaçante la position de la ligne
    :return: Rien
    """
    assert type_position(dico), f"setLignePosition : Les positions sont incorrect."
    assert type(position_ligne) == int, f"setLignePositions : La positions n'est pas un entier."
    dico[LIGNE] = position_ligne

    return None


def setColonnePosition(dico:Position,position_colonne:int)->None:
    """
    Cette fonction modifie la valeur de la colonne de la position avec l’entier passé en paramètre.
    :param dico: Dictionnaire contenant les positions.
    :param position_colonne: Valeur de la position remplaçante la position de la colonne
    :return: Rien
    """
    assert type_position(dico), f"setLignePosition : Les positions sont incorrect."
    assert type(position_colonne) == int, f"setLignePositions : La positions n'est pas un entier."
    dico[COLONNE] = position_colonne

    return None


def incLignePosition(position: Position, valeur: int = 1) -> None:
    """
    Incrémente la ligne de la position d'une valeur donnée (par défaut 1).

    :param position: Dictionnaire de type Position
    :param valeur: entier à ajouter à la ligne
    :return: None
    """
    assert type_position(position), f"incLignePosition : la position est incorrecte."
    assert type(valeur) == int, f"incLignePosition : la valeur n'est pas un entier."
    position[LIGNE] += valeur
    return None


def decLignePosition(position: Position, valeur: int = 1) -> None:
    """
    Décrémente la ligne de la position d'une valeur donnée (par défaut 1).

    :param position: Dictionnaire de type Position
    :param valeur: entier à soustraire à la ligne
    :return: None
    """
    assert type_position(position), f"decLignePosition : la position est incorrecte."
    assert type(valeur) == int, f"decLignePosition : la valeur n'est pas un entier."
    position[LIGNE] -= valeur
    return None


def incColonnePosition(position: Position, valeur: int = 1) -> None:
    """
    Incrémente la colonne de la position d'une valeur donnée (par défaut 1).

    :param position: Dictionnaire de type Position
    :param valeur: entier à ajouter à la colonne
    :return: None
    """
    assert type_position(position), f"incColonnePosition : la position est incorrecte."
    assert type(valeur) == int, f"incColonnePosition : la valeur n'est pas un entier."
    position[COLONNE] += valeur
    return None


def decColonnePosition(position: Position, valeur: int = 1) -> None:
    """
    Décrémente la colonne de la position d'une valeur donnée (par défaut 1).

    :param position: Dictionnaire de type Position
    :param valeur: entier à soustraire à la colonne
    :return: None
    """
    assert type_position(position), f"decColonnePosition : la position est incorrecte."
    assert type(valeur) == int, f"decColonnePosition : la valeur n'est pas un entier."
    position[COLONNE] -= valeur
    return None