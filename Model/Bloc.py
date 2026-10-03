# Model/Bloc.py
#

from Model.CustomTypes import Bloc

# Clé pour stocker le nombre de cellules contigües de même couleur (bloc)
NOMBRE = "nombre"
# Couleur des cellules contigües du bloc
COULEUR = "couleur"
# Booléen permettant de savoir si l'utilisateur a découvert ou non le bloc correspondant
VU = "vu"


def type_bloc(bloc: Bloc) -> bool:
    """
    Détermine si le paramètre peut correspondre ou non à un bloc.

    Un bloc est un dictionnaire contenant 3 clés (NOMBRE, COULEUR, VU) auquelles
    sont associées des valeurs de type (int, int, bool).

    :param bloc: Objet à tester
    :return: True si l'objet correspond à un bloc, False sinon.
    """
    if type(bloc) is not dict:
        return False
    if len(bloc) != 3 or NOMBRE not in bloc or COULEUR not in bloc or VU not in bloc:
        return False
    if type(bloc[NOMBRE]) is not int or bloc[NOMBRE]<=0:
        return False
    if type(bloc[COULEUR]) is not int or bloc[COULEUR]<=0:
        return False
    if type(bloc[VU]) is not bool:
        return False
    return True


def construireBloc(nb_cellule:int,couleur:int)-> Bloc:
    """
    Cette
    fonction construit un dictionnaire correspondant au bloc ayant comme valeurs pour les clés
    respectives NOMBRE et COULEUR, celles des deux paramètres de la fonction et pour la clé VU, la
    valeur False.

    :param nb_cellule: Nombre de cellules contigües de même couleur (bloc)
    :param couleur: La couleur de ces cellules
    :return: un Bloc
    """
    assert type(nb_cellule) is int and nb_cellule > 0, f"construireBloc : le type de nb_cellule n'est pas correct ou bien il n'est pas strictement supérieur à 0."
    assert type(couleur) is int and couleur > 0, f"construireBloc : le type de couleur n'est pas correct ou bien il n'est pas strictement supérieur à 0. "
    return {NOMBRE: nb_cellule,COULEUR: couleur,VU: False}


def getNombreBloc(bloc:Bloc)->int:
    """
    Cette fonction renvoie le nombre de cellules contigües de même couleur dans le dictionnaire bloc.
    :param bloc: Dictionnaire contenant les 3 informations suivantes: NOMBRE,COULEUR,VU.
    :return: Nombre de cellules contigües de même couleur (bloc).
    """
    assert type_bloc(bloc),f"getNombreBloc : le paramètre n'est pas un bloc "
    return bloc[NOMBRE]

def getCouleurBloc(bloc:Bloc)->int:
    """
    Cette fonction renvoie la couleur de ces cellules dans le dictionnaire bloc.
    :param bloc: Dictionnaire contenant les 3 informations suivantes: NOMBRE,COULEUR,VU.
    :return: La couleur de ces cellules (bloc).
    """
    assert type_bloc(bloc),f"getNombreBloc : le paramètre n'est pas un bloc "
    return bloc[COULEUR]

def isVuBloc(bloc:Bloc)->bool:
    """
    Cette fonction renvoie si le bloc a été découvert ou non par l’utilisateur.
    :param bloc: Dictionnaire contenant les 3 informations suivantes: NOMBRE,COULEUR,VU.
    :return: Si le bloc a été découvert ou non.
    """
    assert type_bloc(bloc),f"getNombreBloc : le paramètre n'est pas un bloc "
    return bloc[VU]


def setVuBloc(bloc:Bloc,vu:bool)->None:
    """
    Cette fonction affecte avec le booléen passé en paramètre si le bloc a été vu.
    :param bloc: Dictionnaire contenant les 3 informations suivantes: NOMBRE,COULEUR,VU.
    :param vu: Paramètre qui dira si oui ou non la cellule a été vu.
    :return: Affecte le paramètre a VU.
    """
    assert type_bloc(bloc),f"getNombreBloc : le paramètre n'est pas un bloc "
    assert type(vu) is bool, f"getNombreBloc : le paramètre n'est pas un booléen "
    bloc[VU] = vu
    return None
