# Model/Nonogram.py
from operator import truediv

from Model.Bloc import construireBloc, getNombreBloc, isVuBloc, setVuBloc, NOMBRE
from Model.CustomTypes import ModelImage, LstBlocs, LstLstBlocs, PlayerImage, NbParCouleur, LstCouleurs
from Model.Image import type_image_light
from Model.Cellule import *
from Model.Image import Image
from Model.Joueur import isVuCellJoueur
from Model.Position import LIGNE, COLONNE


def compterBlocsSurLigne(image:ModelImage,num_ligne:int)->LstBlocs:
    """
    Renvoie la liste des blocs présents sur une ligne de l'image.
    :param image: Image de jeu où se trouvent les cellules.
    :param num_ligne: Numéro de la ligne dont on veut connaitre les blocs.
    :return: Liste de blocs (LstBlocs) présents sur la ligne.
    """
    assert type_image_light(image),f"compterBlocsSurLigne : le paramètre ne correspond pas à une image. "
    assert type(num_ligne) is int,f"compterBlocsSurLigne : le paramètre n'est pas un entier."
    blocs = []
    compteur = 0
    couleur_courante = None

    for cellule in image[num_ligne]:
        valeur = cellule[VALEUR]

        if valeur is None or valeur == 0:
            if compteur > 0:
                blocs.append(construireBloc(compteur, couleur_courante))
                compteur = 0
                couleur_courante = None
        else:
            if valeur == couleur_courante:
                compteur += 1
            else:
                if compteur > 0:
                    blocs.append(construireBloc(compteur, couleur_courante))
                couleur_courante = valeur
                compteur = 1

    if compteur > 0:
        blocs.append(construireBloc(compteur, couleur_courante))

    return blocs


def getBlocsLignes(image:Image)-> LstLstBlocs:
    """
    Retourne la liste des blocs pour chaque ligne de l'image.
    L'indice i correspond aux blocs de la ligne i.
    :param image: Image de jeu où se trouvent les cellules.
    :return: Les résultats dans une liste de listes
    """
    liste_resultat = []
    for i in range(len(image)):
        liste_resultat.append(compterBlocsSurLigne(image,i))
    return liste_resultat

def compterBlocsSurColonne(image:ModelImage,num_colonne:int)->LstBlocs:
    """
    Renvoie la liste des blocs présents sur une colonne de l'image.
    :param image: Image de jeu où se trouvent les cellules.
    :param num_colonne: Numéro de la colonne dont on veut connaitre les blocs.
    :return: Liste de blocs (LstBlocs) présents sur la colonne.
    """
    assert type_image_light(image),f"compterBlocsSurLigne : le paramètre ne correspond pas à une image. "
    assert type(num_colonne) is int,f"compterBlocsSurLigne : le paramètre n'est pas un entier."
    blocs = []
    compteur = 0
    couleur_courante = None

    for ligne in range(len(image)):
        cellule = image[ligne][num_colonne]
        valeur = cellule[VALEUR]

        if valeur is None or valeur == 0:
            if compteur > 0:
                blocs.append(construireBloc(compteur, couleur_courante))
                compteur = 0
                couleur_courante = None
        else:
            if valeur == couleur_courante:
                compteur += 1
            else:
                if compteur > 0:
                    blocs.append(construireBloc(compteur, couleur_courante))
                couleur_courante = valeur
                compteur = 1

    if compteur > 0:
        blocs.append(construireBloc(compteur, couleur_courante))

    return blocs


def getBlocsColonnes(image:Image)-> LstLstBlocs:
    """
    Retourne la liste des blocs pour chaque colonne de l'image.
    L'indice i correspond aux blocs de la colonne i.
    :param image: Image de jeu où se trouvent les cellules.
    :return: Les résultats dans une liste de listes
    """
    liste_resultat = []
    for i in range(len(image)):
        liste_resultat.append(compterBlocsSurColonne(image,i))
    return liste_resultat


def isVuImage(img_joueur:PlayerImage)->bool:
    """
    Indique si toutes les cellules du joueur est découverte.
    Une cellule est considérée comme découverte si sa valeur est différente de None.
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :return: True si toutes les cellules sont découverte, False sinon
    """
    res = True
    for i in range(len(img_joueur)):
        for j in range(len(img_joueur[0])):
            position = {LIGNE: i, COLONNE: j}
            if not isVuCellJoueur(img_joueur, position):
                res = False
    return res


def reinitialiserImage (img_joueur:PlayerImage)->None:
    """
    Cette fonction remet toutes les cellules de l’image à l’état non découvert (valeur None).
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :return: Rien
    """
    for i in range(len(img_joueur)):
        for j in range(len(img_joueur[0])):
            cellule = img_joueur[i][j]
            setNonVuCellule(cellule)
    return None

def ligneSansNone(ligne):
    """
    Indique si une ligne (ou une colonne) ne contient plus aucune cellule non découverte.
    :param ligne: Liste de cellules (ligne ou colonne de l'image du joueur).
    :return:True si aucune cellule n'est à None, False sinon.
    """
    res = True
    for cellule in ligne:
        if cellule[VALEUR] is None:
            res = False
    return res


def verifierBlocsDepuisGauche(ligne, lst_blocs) -> bool:
    """
    Vérifie les blocs découverts en parcourant une ligne (ou colonne) depuis la gauche
    (ou le haut pour une colonne).
    :param ligne: Liste de cellules représentant une ligne ou une colonne.
    :param lst_blocs: Liste des blocs associés à cette ligne ou colonne.
    :return: True si au moins un bloc a été marqué comme découvert, False sinon.
    """
    idx_cell = 0
    idx_bloc = 0
    modification = False

    while idx_cell < len(ligne) and idx_bloc < len(lst_blocs):
        if ligne[idx_cell][VALEUR] is None:
            break

        taille = 0
        while idx_cell < len(ligne) and ligne[idx_cell][VALEUR] not in (None, 0):
            taille += 1
            idx_cell += 1

        if taille > 0:
            bloc = lst_blocs[idx_bloc]
            if getNombreBloc(bloc) == taille and not isVuBloc(bloc):
                setVuBloc(bloc, True)
                modification = True
            idx_bloc += 1

        if idx_cell < len(ligne) and ligne[idx_cell][VALEUR] == 0:
            idx_cell += 1

    return modification



def verifierBlocsDepuisDroite(ligne, lst_blocs) -> bool:
    """
    Vérifie les blocs découverts en parcourant une ligne (ou colonne) depuis la droite
    (ou le bas pour une colonne).
    :param ligne: Liste de cellules représentant une ligne ou une colonne.
    :param lst_blocs: Liste des blocs associés à cette ligne ou colonne.
    :return: True si au moins un bloc a été marqué comme découvert, False sinon.
    """
    idx_cell = len(ligne) - 1
    idx_bloc = len(lst_blocs) - 1
    modification = False

    while idx_cell >= 0 and idx_bloc >= 0:
        if ligne[idx_cell][VALEUR] is None:
            break

        taille = 0
        while idx_cell >= 0 and ligne[idx_cell][VALEUR] not in (None, 0):
            taille += 1
            idx_cell -= 1

        if taille > 0:
            bloc = lst_blocs[idx_bloc]
            if getNombreBloc(bloc) == taille and not isVuBloc(bloc):
                setVuBloc(bloc, True)
                modification = True
            idx_bloc -= 1

        if idx_cell >= 0 and ligne[idx_cell][VALEUR] == 0:
            idx_cell -= 1

    return modification



def verifierBlocsLigneImage(img_joueur:PlayerImage,lst_blocs:LstBlocs,num_ligne:int)->bool:
    """
    Vérifie quels blocs d'une ligne sont découverts selon les règles du nonogram.
    Un bloc est découvert si toutes les cellules à gauche ou toutes les cellules
    à droite du bloc sont découvertes (!= None).
    :param img_joueur: Image actuelle du joueur.
    :param lst_blocs: Liste des blocs de définition pour cette ligne.
    :param num_ligne: Numéro de la ligne à vérifier (commençant à 0).
    :return: True si au moins un bloc a été modifié, False sinon.
    """
    ligne = img_joueur[num_ligne]
    modification = False

    # cas 1 : traitement classique depuis les bords
    if verifierBlocsDepuisGauche(ligne, lst_blocs):
        modification = True
    if verifierBlocsDepuisDroite(ligne, lst_blocs):
        modification = True

    # cas 2 : PLUS AUCUNE cellule inconnue sur la ligne
    if ligneSansNone(ligne):
        for bloc in lst_blocs:
            if not isVuBloc(bloc):
                setVuBloc(bloc, True)
                modification = True

    return modification


def extraireColonne(img_joueur: PlayerImage, num_col: int):
    """
    Extrait une colonne de l'image du joueur sous forme de liste de cellules.
    :param img_joueur: Image actuelle du joueur.
    :param num_col: Numéro de la colonne à extraire (commençant à 0).
    :return: Liste des cellules de la colonne, de haut en bas.
    """
    colonne = []
    for ligne in img_joueur:
        colonne.append(ligne[num_col])
    return colonne


def verifierBlocsColonneImage(img_joueur: PlayerImage,lst_blocs: LstBlocs,num_col: int) -> bool:
    """
    Vérifie quels blocs d'une colonne sont découverts selon les règles du nonogram.
    Un bloc est découvert uniquement si toutes les cellules au-dessus ou toutes les
    cellules en dessous sont découvertes (!= None).

    :param img_joueur: L'image actuelle du joueur.
    :param lst_blocs: La liste des blocs de définition pour cette colonne.
    :param num_col: Le numéro de la colonne (commençant à 0).
    :return: True si au moins un bloc a été modifié, False sinon.
    """
    colonne = extraireColonne(img_joueur, num_col)
    modification = False

    if verifierBlocsDepuisGauche(colonne, lst_blocs):
        modification = True
    if verifierBlocsDepuisDroite(colonne, lst_blocs):
        modification = True

    if ligneSansNone(colonne):
        for bloc in lst_blocs:
            if not isVuBloc(bloc):
                setVuBloc(bloc, True)
                modification = True

    return modification


def isLigneDecouverteImage(img_joueur: PlayerImage, lst_blocs: LstBlocs, num_ligne: int) -> bool:
    """
    Vérifie si tous les blocs de la ligne spécifiée ont été découverts.
    :param img_joueur: L'image du joueur (liste de listes de cellules)
    :param lst_blocs: La liste des blocs pour chaque ligne (liste de listes d'entiers)
    :param num_ligne: Le numéro de la ligne (commençant à 0)
    :return: True si tous les blocs sont découverts, False sinon.
    """
    res = False

    somme_blocs = 0
    for bloc in lst_blocs:
        somme_blocs += getNombreBloc(bloc)

    ligne = img_joueur[num_ligne]
    cellules_remplies = 0
    for cellule in ligne:
        if cellule[VALEUR] is not None and cellule[VALEUR] != 0:
            cellules_remplies += 1

    if cellules_remplies == somme_blocs:
        res = True

    return res


def getCellsNonVuesLigneImage(img_joueur:PlayerImage,num_ligne:int)->list[int]:
    """
    Retourne la liste des numéros de colonne des cellules non découvertes (VALEUR == None) dans la ligne spécifiée.
    Si toutes les cellules sont découvertes, retourne une liste vide.
    :param img_joueur: L'image du joueur (liste de listes de cellules)
    :param num_ligne: Le numéro de la ligne (commençant à 0)
    :return: Liste des indices de colonnes des cellules non découvertes
    """
    lst_num_colonne= []
    ligne = img_joueur[num_ligne]
    for i in range(len(ligne)):
        if ligne[i][VALEUR] is None:
            lst_num_colonne.append(i)
    return lst_num_colonne


def isColonneDecouverteImage(img_joueur: PlayerImage, lst_blocs: LstBlocs, num_colonne: int) -> bool:
    """
    Vérifie si tous les blocs de la colonne spécifiée ont été découverts.
    :param img_joueur: L'image du joueur (liste de listes de cellules)
    :param lst_blocs: La liste des blocs pour chaque colonne (liste de listes d'entiers)
    :param num_colonne: Le numéro de la colonne (commençant à 0)
    :return: True si tous les blocs sont découverts, False sinon.
    """

    res = False

    somme_blocs = 0
    for bloc in lst_blocs:
        somme_blocs += getNombreBloc(bloc)

    colonne = extraireColonne(img_joueur,num_colonne)
    cellules_remplies = 0
    for cellule in colonne:
        if cellule[VALEUR] is not None and cellule[VALEUR] != 0:
            cellules_remplies += 1

    if cellules_remplies == somme_blocs:
        res = True

    return res


def getCellsNonVuesColonneImage(img_joueur:PlayerImage,num_colonne:int)->list[int]:
    """
    Retourne la liste des numéros de ligne des cellules non découvertes (VALEUR == None) dans la colonne spécifiée.
    Si toutes les cellules sont découvertes, retourne une liste vide.
    :param img_joueur: L'image du joueur (liste de listes de cellules)
    :param num_colonne: Le numéro de la colonne (commençant à 0)
    :return: Liste des indices de ligne des cellules non découvertes
    """
    lst_num_ligne= []
    colonne = extraireColonne(img_joueur,num_colonne)
    for i in range(len(colonne)):
        if colonne[i][VALEUR] is None:
            lst_num_ligne.append(i)
    return lst_num_ligne


def getNbParCouleur(dim_image:int,lst_lst_bloc:LstLstBlocs)->NbParCouleur:
    """
    Associe à chaque couleur le nombre total de cellules de cette couleur
    (y compris la couleur 0 pour les cellules vides).
    :param dim_image: Un entier correspondant à la dimension de l’image.
    :param lst_lst_bloc:Une liste de listes de blocs (pouvant correspondre à la liste des blocs des lignes ou la liste des blocs des colonnes).
    :return: Le dictionnaire associant à chaque couleur le nombre de cellules portant cette couleur ainsi que cellules vides.
    """
    nb_par_couleur: NbParCouleur = {}
    total_colore = 0

    for lst_blocs in lst_lst_bloc:
        for bloc in lst_blocs:
            couleur = bloc[COULEUR]
            nombre = bloc[NOMBRE]

            nb_par_couleur[couleur] = nb_par_couleur.get(couleur, 0) + nombre
            total_colore += nombre

    nb_total_cellules = dim_image * dim_image
    nb_par_couleur[0] = nb_total_cellules - total_colore

    return nb_par_couleur


def getCouleursVuImage(img_joueur: PlayerImage,nb_par_couleur: NbParCouleur) -> LstCouleurs:
    """
    Retourne la liste des couleurs pour lesquelles toutes les cellules
    ont été découvertes par le joueur.
    :param img_joueur: L'image du joueur (liste de listes de cellules).
    :param nb_par_couleur: Le dictionnaire associant couleur et nombre de cellules.
    :return:Une liste (type/alias LstCouleurs) les couleurs pour lesquelles toutes les cellules portant cette couleur
    sont « découvertes ». Si aucune couleur n’a été totalement découverte, la fonction retourne une liste vide.
    """
    couleurs_vues = {}

    for ligne in img_joueur:
        for cellule in ligne:
            couleur = cellule[VALEUR]
            if couleur is not None:
                if couleur in couleurs_vues:
                    couleurs_vues[couleur] += 1
                else:
                    couleurs_vues[couleur] = 1

    couleurs_completes = []

    for couleur, nb_total in nb_par_couleur.items():
        if couleur in couleurs_vues and couleurs_vues[couleur] == nb_total:
            couleurs_completes.append(couleur)

    return couleurs_completes






