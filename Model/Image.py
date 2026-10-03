# Model/Image.py

from Model.CustomTypes import Image
from Model.Cellule import *
from Model.Position import *

#
# Gestion simple des nonograms
#
# Accès simple en lecture et en écriture à une "image"
# Création d'une "image"...
#


def type_image_light(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    Version light : Ne vérifie pas le contenu des listes...

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if type(img) is not list:
        return False
    wrong = "Erreur !"
    if len(img) == 0:
        return False
    if type(img[0]) is not list:
        return False
    n_c = len(img[0])
    if n_c != len(img):
        return False
    if next((wrong for line in img if type(line) is not list or len(line) != n_c), True) == wrong:
        return False
    return True


def type_image_full(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    En plus de la version light, vérifie que le contenu des listes correspond bien à une cellule.

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if not type_image_light(img):
        return False
    wrong = "Erreur !"
    if next((wrong for line in img for c in line if c is not None and not type_cellule(c)), True) == wrong:
        return False
    return True


def getCellImage(image:Image,pos:Position)->Cellule:
    """
    Retourne la cellule correspondant à la position dans l'image.
    :param image: Image (liste de listes de cellules)
    :param pos: Position (ligne, colonne)
    :return: Cellule correspondante
    """
    assert type_image_light(image),f"getCellImage : le type d'image est incorrecte."
    assert type_position(pos), f"getCellImage : la position est incorrecte."
    return image[pos[LIGNE]][pos[COLONNE]]


def setCellImage(image:Image,pos:Position,entier:int|None)->None:
    """
    remplace la couleur de la cellule à la position indiquée dans l’image passée en paramètre par l’entier donné.
    :param image: Image (liste de listes de cellules)
    :param pos: Position (ligne, colonne)
    :param entier: un entier qui attribue la couleur.
    :return: Affecte la nouvelle couleur à la Cellule correspondante
    """
    assert type_image_light(image),f"setCellImage : le type d'image est incorrecte."
    assert type_position(pos), f"setCellImage : la position est incorrecte."
    assert type(entier)== int or entier is None, f"setCellImage : la valeur de l'entier est incorrecte."

    image[pos[LIGNE]][pos[COLONNE]][VALEUR] = entier
    return None


def creerImage(taille_image:int,lst_image: list[list[int]]|None = None)->Image:
    """
    fonction qui crée une image de taille_image dimensions
    :param taille_image: taille de l'image (au carré)
    :param lst_image: Liste contenant des entiers représentant la couleur ou bien None.
    :return: Une image contenant des cellules dont la valeur est None si le deuxième paramètre vaut None, ou les valeurs de la liste de listes contenue dans le second paramètre dans le cas contraire.
    """
    assert type(taille_image)== int and 5<= taille_image <= 20, f"creerImage : le type de taille_image est incorrecte ou bien, inférieur à 5 ou supérieur à 20."
    if lst_image is not None:
        assert type_image_light(lst_image), f"creerImage : le paramètre lst_image est incorrect."
        assert len(lst_image) == taille_image,f"creerImage :  la taille de ces listes correspond pas à la valeur du premier paramètre."
    image = []
    for i in range(taille_image):
        ligne = []

        for j in range(taille_image):
            if lst_image is None:
                ligne.append(construireCellule())
            else:
                ligne.append({VALEUR: lst_image[i][j]})

        image.append(ligne)

    return image