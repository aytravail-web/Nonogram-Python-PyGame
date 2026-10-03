# Model/Joueur.py

from Model.CustomTypes import *
from Model.Image import *
from Model.Cellule import *
from Model.Bloc import *
from Model.Suggestion import *
from Model.Nonogram import *


def isVuCellJoueur(img_joueur:PlayerImage,position:Position)->bool:
    """
    Indique si la cellule du joueur à la position donnée est découverte.
    Une cellule est considérée comme découverte si sa valeur est différente de None.
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :param position: Position de la cellule (ligne, colonne)
    :return: True si la cellule est découverte, False sinon
    """
    res = False
    cellule = img_joueur[position[LIGNE]][position[COLONNE]]
    if cellule[VALEUR] is not None:
        res = True
    return res

def isCouleurCorrecteImage(image:ModelImage,position:Position,couleur:int)->bool:
    """
    Indique si la cellule à la position donnée dans l'image contient la couleur spécifiée.
    :param image: Image du jeu
    :param position: Position de la cellule (ligne, colonne)
    :param couleur: Couleur à vérifier
    :return: True si la cellule contient cette couleur, False sinon
    """
    res = False
    cellule = image[position[LIGNE]][position[COLONNE]]
    if cellule[VALEUR] == couleur:
        res = True
    return res

def isLigneNonVueImage(img_joueur:PlayerImage,num_ligne)->bool:
    """
    Fonction qui informe si la ligne a été découverte ou non en renvoyant un booléen.
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :param num_ligne: Numéro de la ligne dont on veut savoir si elle a été découverte.
    :return: True si la ligne ne possède aucune cellule découverte, False sinon.
    """
    res=True
    ligne = img_joueur[num_ligne]
    for cellule in ligne:
        if cellule[VALEUR] is not None:
            res =  False
    return res

def extraireColonne(img_joueur: PlayerImage, num_colonne: int):
    """
    Extrait une colonne de l'image du joueur sous forme de liste de cellules.
    :param img_joueur: Image du joueur
    :param num_colonne: Numéro de la colonne
    :return: Liste des cellules de la colonne
    """
    colonne = []
    for ligne in img_joueur:
        colonne.append(ligne[num_colonne])
    return colonne



def isColonneNonVueImage(img_joueur:PlayerImage,num_colonne)->bool:
    """
    Fonction qui informe si la colonne a été découverte ou non en renvoyant un booléen.
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :param num_colonne: Numéro de la colonne dont on veut savoir si elle a été découverte.
    :return: True si la colonne ne possède aucune cellule découverte, False sinon.
    """
    res = True
    colonne = extraireColonne(img_joueur, num_colonne)
    for cellule in colonne:
        if cellule[VALEUR] is not None:
            res =  False
    return res

def appliquerMonoRecouvrementLigne(img_joueur:PlayerImage,num_ligne:int,lst_ligne_blocs:LstBlocs)->LstSuggestions:
    """
    Applique la méthode de recouvrement simple sur une ligne non découverte.
    :param img_joueur: Image du joueur
    :param num_ligne: Numéro de la ligne
    :param lst_ligne_blocs: Liste des blocs de la ligne
    :return: Liste de suggestions pour ligne.
    """
    lst_suggestions = []
    if isLigneNonVueImage(img_joueur, num_ligne):

        taille_ligne = len(img_joueur[num_ligne])
        taille_blocs = 0
        for bloc in lst_ligne_blocs:
            taille_blocs = taille_blocs + bloc[NOMBRE]

        if len(lst_ligne_blocs) > 1:
            taille_blocs = taille_blocs + (len(lst_ligne_blocs) - 1)

        cellules_restantes = taille_ligne - taille_blocs
        position = 0

        for bloc in lst_ligne_blocs:
            taille_bloc = bloc[NOMBRE]
            nb_cellules_sures = taille_bloc - cellules_restantes

            if nb_cellules_sures > 0:
                for i in range(nb_cellules_sures):
                    suggestion = {POSITION: {LIGNE: num_ligne, COLONNE: position + cellules_restantes + i},COULEUR: 1}
                    lst_suggestions.append(suggestion)
            position = position + taille_bloc + 1

    return lst_suggestions


def appliquerMonoRecouvrementColonne(img_joueur:PlayerImage,num_colonne:int,lst_colonne_blocs:LstBlocs)->LstSuggestions:
    """
    Applique la méthode de recouvrement simple sur une colonne non découverte.
    :param img_joueur: Image du joueur
    :param num_colonne: Numéro de la colonne
    :param lst_colonne_blocs: Liste des blocs de la colonne
    :return: Liste de suggestions pour colonne.
    """
    lst_suggestions = []
    if isColonneNonVueImage(img_joueur, num_colonne):
        taille_colonne = len(img_joueur)
        taille_blocs = 0
        for bloc in lst_colonne_blocs:
            taille_blocs = taille_blocs + bloc[NOMBRE]

        if len(lst_colonne_blocs) > 1:
            taille_blocs = taille_blocs + (len(lst_colonne_blocs) - 1)

        cellules_restantes = taille_colonne - taille_blocs
        position = 0
        for bloc in lst_colonne_blocs:
            taille_bloc = bloc[NOMBRE]
            nb_cellules_sures = taille_bloc - cellules_restantes

            if nb_cellules_sures > 0:
                for i in range(nb_cellules_sures):
                    suggestion = {POSITION: {LIGNE: position + cellules_restantes + i,COLONNE: num_colonne},COULEUR: 1}
                    lst_suggestions.append(suggestion)

            position = position + taille_bloc + 1

    return lst_suggestions


def appliquerMonoRecouvrement(img_joueur: PlayerImage,lst_blocs_lignes: LstLstBlocs,lst_blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la méthode de recouvrement simple sur toutes les lignes
    et toutes les colonnes de l'image du joueur.
    :param img_joueur: Image du joueur (liste de listes de cellules)
    :param lst_blocs_lignes: Liste des blocs pour chaque ligne
    :param lst_blocs_colonnes: Liste des blocs pour chaque colonne
    :return: Liste de toutes les suggestions possibles
    """

    lst_suggestions = []
    for num_ligne in range(len(lst_blocs_lignes)):
        suggestions_ligne = appliquerMonoRecouvrementLigne(img_joueur,num_ligne,lst_blocs_lignes[num_ligne])
        for suggestion in suggestions_ligne:
            lst_suggestions.append(suggestion)

    for num_colonne in range(len(lst_blocs_colonnes)):
        suggestions_colonne = appliquerMonoRecouvrementColonne(img_joueur,num_colonne,lst_blocs_colonnes[num_colonne])
        for suggestion in suggestions_colonne:
            lst_suggestions.append(suggestion)

    return lst_suggestions


def isRangeeVide(rangee: Rangee) -> bool:
    """
    Vérifie si une rangée ne contient aucune cellule découverte.
    :param rangee: La rangée a vérifié
    :return: True si la rangée est vide (aucune cellule découverte), False sinon.
    """
    res = True
    for cellule in rangee:
        if cellule[VALEUR] is not None:
            res = False
    return res

def isRangeeDecouverte(rangee: Rangee) -> bool:
    """
    Vérifie si une rangée est entièrement découverte.
    :param rangee: La rangée a vérifié
    :return: True si toutes les cellules de la rangée sont découvertes, False sinon.
    """
    res = True
    for cellule in rangee:
        if cellule[VALEUR] is None:
            res = False
    return res

def appliquerMonoGlueBordRangee(rangee: Rangee, lst_blocs: LstBlocs) -> LstIndexCouleurs:
    """
    Applique la "glue du bord" sur le bord gauche d'une rangée (ligne ou colonne).
    :param rangee: La rangée (ligne ou colonne) à traiter.
    :param lst_blocs: Liste des blocs correspondant à cette rangée.
    :return: Liste des suggestions sous forme de LstIndexCouleurs ou une liste vide si aucune suggestion.
    """
    suggestions = []
    idx = 0
    res = True
    if isRangeeVide(rangee) or isRangeeDecouverte(rangee):
        res = False

    if res:
        while idx < len(rangee):
            cellule = rangee[idx]

            if cellule[VALEUR] is None:
                suggestions.append((idx, 1))
                idx += 1
            elif cellule[VALEUR] == 0:
                idx += 1
            elif cellule[VALEUR] != 0:
                for bloc in lst_blocs:
                    if bloc[NOMBRE] > 1:
                        suggestions.append((idx, 1))
                        idx += 1
                idx += 1
    return suggestions



def indexCouleursToSuggestions(idx_color: LstIndexCouleurs, num_rangee: int, is_ligne: bool) -> LstSuggestions:
    """
    Transforme une liste d'index et couleurs en suggestions.
    :param idx_color: Liste d'index et couleurs (type LstIndexCouleurs).
    :param num_rangee: Numéro de la ligne ou de la colonne.
    :param is_ligne: Booléen indiquant si la transformation concerne une ligne (True) ou une colonne (False).
    :return: Liste de suggestions construite à partir des index et couleurs.
    """
    suggestions = []
    for i in range(len(idx_color)):
        idx = idx_color[i][0]
        couleur = idx_color[i][1]
        if is_ligne:
            suggestions.append({POSITION: {LIGNE: num_rangee, COLONNE: idx}, COULEUR: couleur})
        else:
            suggestions.append({POSITION: {LIGNE: idx, COLONNE: num_rangee}, COULEUR: couleur})
    return suggestions

def getLigneImage(image: PlayerImage, li: int) -> Rangee:
    """
    Retourne la ligne li de l'image.
    :param image: Image du joueur (liste de listes de cellules)
    :param li: Numéro de la ligne à récupérer
    :return: La rangée (ligne) correspondante à li
    """
    return image[li]

def getLigneInverseImage(image: PlayerImage, li: int) -> Rangee:
    """
    Retourne la ligne li inversée de l'image.
    :param image: Image du joueur (liste de listes de cellules)
    :param li: Numéro de la ligne à inverser
    :return: La rangée (ligne) inversée correspondante à li
    """
    ligne_inversee = []
    for i in range(len(image[li]) - 1, -1, -1):
        ligne_inversee.append(image[li][i])
    return ligne_inversee

def getLstBlocsInverse(blocs: LstBlocs) -> LstBlocs:
    """
    Retourne la liste inversée des blocs.
    :param blocs: Liste des blocs à inverser
    :return: La liste des blocs inversée
    """
    blocs_inverses = []
    for i in range(len(blocs) - 1, -1, -1):
        blocs_inverses.append(blocs[i])
    return blocs_inverses

def getColonneImage(image: PlayerImage, co: int) -> Rangee:
    """
    Retourne la colonne co de l'image.
    :param image: Image du joueur (liste de listes de cellules)
    :param co: Numéro de la colonne à récupérer
    :return: La rangée (colonne) correspondante à co
    """
    colonne = []
    for ligne in image:
        colonne.append(ligne[co])
    return colonne

def getColonneInverseImage(image: PlayerImage, co: int) -> Rangee:
    """
    Retourne la colonne co inversée de l'image.
    :param image: Image du joueur (liste de listes de cellules)
    :param co: Numéro de la colonne à inverser
    :return: La rangée (colonne) inversée correspondante à co
    """
    colonne_inversee = []
    colonne = getColonneImage(image, co)
    for i in range(len(colonne) - 1, -1, -1):
        colonne_inversee.append(colonne[i])
    return colonne_inversee

def getIndexInverseDeIndexCouleurs(idx_color: LstIndexCouleurs, dim: int) -> LstIndexCouleurs:
    """
    Calcule la valeur réelle des indices après un retournement d'une ligne/colonne.
    :param idx_color: Liste d'index et couleurs sous forme de tuples (index, couleur).
    :param dim: Dimension de l'image (nombre de lignes/colonnes).
    :return: Liste des index réels après le retournement, sous forme de LstIndexCouleurs.
    """
    idx_inverses = []
    for idx, couleur in idx_color:
        idx_inverses.append((dim - 1 - idx, couleur))
    return idx_inverses


def appliquerMonoGlueBord(image: PlayerImage, lst_blocs_lignes: LstLstBlocs,lst_blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la "glue du bord" pour les lignes et colonnes (y compris les versions inversées de celles-ci) de l'image du joueur.
    :param image: Image du joueur (type PlayerImage), un tableau 2D représentant l'état du jeu.
    :param lst_blocs_lignes: Liste des blocs pour chaque ligne de l'image.
    :param lst_blocs_colonnes: Liste des blocs pour chaque colonne de l'image.
    :return: Liste de toutes les suggestions retournées (type LstSuggestions).
    """
    suggestions = []
    for num_ligne in range(len(image)):
        suggestions_ligne = appliquerMonoGlueBordRangee(image[num_ligne], lst_blocs_lignes[num_ligne])
        suggestions.extend(suggestions_ligne)

    for num_ligne in range(len(image)):
        ligne_inverse = getLigneInverseImage(image, num_ligne)
        blocs_ligne_inverse = getLstBlocsInverse(lst_blocs_lignes[num_ligne])
        suggestions_ligne_inverse = appliquerMonoGlueBordRangee(ligne_inverse, blocs_ligne_inverse)
        suggestions.extend(suggestions_ligne_inverse)

    for num_colonne in range(len(image[0])):
        colonne = getColonneImage(image, num_colonne)
        blocs_colonne = lst_blocs_colonnes[num_colonne]
        suggestions_colonne = appliquerMonoGlueBordRangee(colonne, blocs_colonne)
        suggestions.extend(suggestions_colonne)

    for num_colonne in range(len(image[0])):
        colonne_inverse = getColonneInverseImage(image, num_colonne)
        blocs_colonne_inverse = getLstBlocsInverse(lst_blocs_colonnes[num_colonne])
        suggestions_colonne_inverse = appliquerMonoGlueBordRangee(colonne_inverse, blocs_colonne_inverse)
        suggestions.extend(suggestions_colonne_inverse)

    return suggestions

def appliquerBoucheTrouRangee(rangee: Rangee, lst_blocs: LstBlocs) -> LstSuggestions:
    """
    Applique la méthode de "bouche trou" à une rangée (ligne ou colonne) pour marquer les cellules vides comme étant des trous.
    :param rangee: La rangée (ligne ou colonne) à traiter.
    :param lst_blocs: Liste des blocs correspondant à cette rangée.
    :return: Liste des suggestions de trous à marquer comme vides.
    """
    suggestions = []
    min_cells = min([bloc[NOMBRE] for bloc in lst_blocs])
    if min_cells > 1:
        idx = 0
        while idx < len(rangee):
            if rangee[idx][VALEUR] is None:
                start_idx = idx
                while idx < len(rangee) and rangee[idx][VALEUR] is None:
                    idx += 1
                end_idx = idx
                if end_idx - start_idx < min_cells:
                    for i in range(start_idx, end_idx):
                        suggestions.append({POSITION: {LIGNE: start_idx, COLONNE: i}, COULEUR: 0})
            idx += 1
    return suggestions



def appliquerBoucheTrou(image: PlayerImage, lst_blocs_lignes: LstLstBlocs, lst_blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la méthode de bouche trou sur les lignes et les colonnes de l'image du joueur.
    :param image: Image du joueur (type PlayerImage), un tableau 2D représentant l'état du jeu.
    :param lst_blocs_lignes: Liste des blocs pour chaque ligne de l'image.
    :param lst_blocs_colonnes: Liste des blocs pour chaque colonne de l'image.
    :return: Liste de toutes les suggestions pour les trous à boucher.
    """
    suggestions = []

    for num_ligne in range(len(image)):
        suggestions_ligne = appliquerBoucheTrouRangee(image[num_ligne], lst_blocs_lignes[num_ligne])
        suggestions.extend(suggestions_ligne)

    for num_colonne in range(len(image[0])):
        colonne = getColonneImage(image, num_colonne)
        blocs_colonne = lst_blocs_colonnes[num_colonne]
        suggestions_colonne = appliquerBoucheTrouRangee(colonne, blocs_colonne)
        suggestions.extend(suggestions_colonne)

    return suggestions

def plusDeMonoSuggestions(image: PlayerImage, lst_lignes_blocs: LstLstBlocs, lst_colonnes_blocs: LstLstBlocs) -> LstSuggestions:
    """
    Génère des suggestions supplémentaires basées sur des cas simples, comme des lignes ou colonnes avec un ou deux blocs.
    :param image: Image du joueur (type PlayerImage)
    :param lst_lignes_blocs: Liste des blocs des lignes
    :param lst_colonnes_blocs: Liste des blocs des colonnes
    :return: Liste de suggestions supplémentaires
    """
    lst_suggestions = []

    for num_ligne in range(len(lst_lignes_blocs)):
        if len(lst_lignes_blocs[num_ligne]) <= 2:
            suggestions_ligne = appliquerMonoRecouvrementLigne(image, num_ligne, lst_lignes_blocs[num_ligne])
            lst_suggestions.extend(suggestions_ligne)

    for num_colonne in range(len(lst_colonnes_blocs)):
        if len(lst_colonnes_blocs[num_colonne]) <= 2:
            suggestions_colonne = appliquerMonoRecouvrementColonne(image, num_colonne, lst_colonnes_blocs[num_colonne])
            lst_suggestions.extend(suggestions_colonne)

    return lst_suggestions



def appliquerRecouvrementLigne(img_joueur: PlayerImage, num_ligne: int, lst_ligne_blocs: LstBlocs) -> LstSuggestions:
    """
    Applique le recouvrement sur une ligne pour le jeu en couleur.
    Gère les couleurs et les espaces (espace obligatoire seulement entre deux blocs de même couleur).
    :param img_joueur: Image du joueur
    :param num_ligne: Numéro de la ligne
    :param lst_ligne_blocs: Liste des blocs de la ligne
    :return: Liste de suggestions pour la ligne.
    """
    lst_suggestions = []
    if isLigneNonVueImage(img_joueur, num_ligne):
        taille_ligne = len(img_joueur[num_ligne])

        taille_min_blocs = 0
        for i in range(len(lst_ligne_blocs)):
            taille_min_blocs += getNombreBloc(lst_ligne_blocs[i])
            if i < len(lst_ligne_blocs) - 1:
                if getCouleurBloc(lst_ligne_blocs[i]) == getCouleurBloc(lst_ligne_blocs[i + 1]):
                    taille_min_blocs += 1

        cellules_restantes = taille_ligne - taille_min_blocs
        position = 0

        for i in range(len(lst_ligne_blocs)):
            bloc = lst_ligne_blocs[i]
            taille_bloc = getNombreBloc(bloc)
            couleur_bloc = getCouleurBloc(bloc)

            nb_cellules_sures = taille_bloc - cellules_restantes

            if nb_cellules_sures > 0:
                for k in range(nb_cellules_sures):
                    suggestion = {POSITION: {LIGNE: num_ligne, COLONNE: position + cellules_restantes + k},COULEUR: couleur_bloc}
                    lst_suggestions.append(suggestion)

            position += taille_bloc

            if i < len(lst_ligne_blocs) - 1:
                if getCouleurBloc(lst_ligne_blocs[i]) == getCouleurBloc(lst_ligne_blocs[i + 1]):
                    position += 1

    return lst_suggestions


def appliquerRecouvrementColonne(img_joueur: PlayerImage, num_colonne: int,lst_colonne_blocs: LstBlocs) -> LstSuggestions:
    """
    Applique le recouvrement sur une colonne pour le jeu en couleur.
    :param img_joueur: Image du joueur
    :param num_colonne: Numéro de la colonne
    :param lst_colonne_blocs: Liste des blocs de la colonne
    :return: Liste de suggestions pour la colonne.
    """
    lst_suggestions = []
    if isColonneNonVueImage(img_joueur, num_colonne):
        taille_colonne = len(img_joueur)
        taille_min_blocs = 0
        for i in range(len(lst_colonne_blocs)):
            taille_min_blocs += getNombreBloc(lst_colonne_blocs[i])
            if i < len(lst_colonne_blocs) - 1:
                if getCouleurBloc(lst_colonne_blocs[i]) == getCouleurBloc(lst_colonne_blocs[i + 1]):
                    taille_min_blocs += 1

        cellules_restantes = taille_colonne - taille_min_blocs
        position = 0
        for i in range(len(lst_colonne_blocs)):
            bloc = lst_colonne_blocs[i]
            taille_bloc = getNombreBloc(bloc)
            couleur_bloc = getCouleurBloc(bloc)

            nb_cellules_sures = taille_bloc - cellules_restantes

            if nb_cellules_sures > 0:
                for k in range(nb_cellules_sures):
                    suggestion = {POSITION: {LIGNE: position + cellules_restantes + k, COLONNE: num_colonne},COULEUR: couleur_bloc}
                    lst_suggestions.append(suggestion)

            position += taille_bloc
            if i < len(lst_colonne_blocs) - 1:
                if getCouleurBloc(lst_colonne_blocs[i]) == getCouleurBloc(lst_colonne_blocs[i + 1]):
                    position += 1

    return lst_suggestions


def appliquerRecouvrement(img_joueur: PlayerImage, lst_blocs_lignes: LstLstBlocs,lst_blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la méthode de recouvrement (version couleur) sur toutes les lignes et colonnes.
    :param img_joueur: Image du joueur
    :param lst_blocs_lignes: Blocs des lignes
    :param lst_blocs_colonnes: Blocs des colonnes
    :return: Liste complète des suggestions
    """
    lst_suggestions = []


    for num_ligne in range(len(lst_blocs_lignes)):
        sug_ligne = appliquerRecouvrementLigne(img_joueur, num_ligne, lst_blocs_lignes[num_ligne])
        lst_suggestions.extend(sug_ligne)


    for num_col in range(len(lst_blocs_colonnes)):
        sug_col = appliquerRecouvrementColonne(img_joueur, num_col, lst_blocs_colonnes[num_col])
        lst_suggestions.extend(sug_col)

    return lst_suggestions