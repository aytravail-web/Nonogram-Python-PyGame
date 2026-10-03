# Model/Suggestion.py

# Suggestions de coups à jouer modélisés par un dictionnaire à deux clés :
# - POSITION : Position dans l'image
# - COULEUR : Couleur à placer (la couleur transparente, 0, étant acceptée)

# Deux clés associées au dictionnaire représentant une suggestion :
POSITION = "position"
COULEUR = "couleur"


from Model.CustomTypes import *
from Model.Position import *

def type_suggestion(suggestion: Suggestion) -> bool:
    """
    Détermine si le paramètre correspond ou non à une suggestion

    :param suggestion: Objet à tester
    :return: True s'il correspond à une suggestion, False sinon
    """
    if type(suggestion) is not dict:
        return False
    if POSITION not in suggestion or COULEUR not in suggestion:
        return False
    if not type_position(suggestion[POSITION]):
        return False
    if type(suggestion[COULEUR]) is not int:
        return False
    return True


def construireSuggestion(pos:Position,couleur_sug:int)->dict:
    """
    Construit une suggestion.
    :param pos: Position de la suggestion.
    :param couleur_sug: Couleur de la suggestion.
    :return: La suggestion sous un dictionnaire.
    """
    assert type_position(pos),f"construiSuggestion : le parametre {pos}ne correspond pas à une position"
    assert type(couleur_sug) is int, f"construiSuggestion : le parametre {couleur_sug}ne correspond pas à un entier"
    return {POSITION: pos, COULEUR: couleur_sug}


def getPositionSuggestion(suggestion:Suggestion)->Position:
    """
    Donne la positon de la suggestion.
    :param suggestion: Dictionnaire contenant la position et la couleur suggérée.
    :return: La position contenue dans la suggestion.
    """
    assert type_suggestion(suggestion), f"getSuggestion : le parametre {suggestion}ne correspond pas à un dictionnaire"
    return suggestion[POSITION]

def getCouleurSuggestion(suggestion:Suggestion)->COULEUR:
    """
    Donne la couleur de la suggestion.
    :param suggestion: Dictionnaire contenant la position et la couleur suggérée.
    :return: La couleur contenue dans la suggestion.
    """
    assert type_suggestion(suggestion), f"getSuggestion : le parametre {suggestion}ne correspond pas à un dictionnaire"
    return suggestion[COULEUR]