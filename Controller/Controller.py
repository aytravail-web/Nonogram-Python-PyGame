from __future__ import annotations

from random import randint

from Model.Cellule import *
from Model.CustomTypes import *
from Model.Data import *
from Model.Bloc import *
from Model.Image import *
from Model.Suggestion import *
from Model.Nonogram import *
from Model.Joueur import *

import pygame


def __creerImage(size: int, data: list[list[int]] = None) -> Image | None:
    print("Fonction creerImage manquante !")
    return [[{VALEUR: 0}] * size]*size


def __getBlocsLignes(image: ModelImage) -> LstLstBlocs:
    print("Fonction getBlocsLignes manquante !")
    return [[]]*len(image)


def __getBlocsColonnes(image: ModelImage) -> LstLstBlocs:
    print("Fonction getBlocsColonnes manquante !")
    return [[]]*len(image)

def __isVuCellJoueur(image: Image, pos: Position) -> bool:
    print("Fonction isVuCellJoueur manquante !")
    return True

def __isCouleurCorrecteImage(image: Image, pos: Position) -> bool:
    print("Fonction isCouleurCorrecteImage manquante !")
    return False

def __setCellImage(image:Image, pos: Position, color: int) -> None:
    print("Fonction setCellImage manquante !")
    return None

def __reinitialiserImage(image: Image) -> None:
    print("Fonction reinitialiserImage manquante !")
    return None

def __isVuImage(image: Image) -> bool:
    print("Fonction isVuImage manquante !")
    return False

def __verifierBlocsLigneImage(image: Image, blocs: LstBlocs, li: int) -> bool:
    print("Fonction verifierBlocsLigneImage manquante !")
    return False

def __verifierBlocsColonneImage(image: Image, blocs: LstBlocs, li: int) -> bool:
    print("Fonction verifierBlocsColonneImage manquante !")
    return False

def __isLigneDecouverteImage(image: Image, blocs: LstBlocs, li: int) -> bool:
    print("Fonction isLigneDecouverte manquante !")
    return False

def __isColonneDecouverteImage(image: Image, blocs: LstBlocs, co: int) -> bool:
    print("Fonction isColonneDecouverte manquante !")
    return False

def __getCellsNonVuesLigneImage(image: Image, li: int) -> list[int]:
    print("Fonction getCellsNonVuesLigneImage manquante !")
    return []

def __getCellsNonVuesColonneImage(image: Image, li: int) -> list[int]:
    print("Fonction getCellsNonVuesColonneImage manquante !")
    return []

def __getNbParCouleur(size: int, blocs: LstLstBlocs) -> NbParCouleur:
    print("Fonction getNbParCouleur manquante !")
    return {}

def __getCouleursVuImage(image: PlayerImage, nbColors: NbParCouleur) -> LstCouleurs:
    print("Fonction getCouleursVuImage manquante !")
    return []

def __appliquerMonoRecouvrement(image: PlayerImage, blocsLignes: LstLstBlocs, blocsColonnes: LstLstBlocs) -> LstSuggestions:
    print("Fonction appliquerMonoRecouvrement manquante !")
    return []

def __appliquerRecouvrement(image: PlayerImage, blocsLignes: LstLstBlocs, blocsColonnes: LstLstBlocs) -> LstSuggestions:
    print("Fonction appliquerRecouvrement manquante !")
    return []

def __appliquerMonoGlueBord(image: PlayerImage, blocsLignes: LstLstBlocs, blocsColonnes: LstLstBlocs) -> LstSuggestions:
    print("Fonction appliquerMonoGlueBord manquante !")
    return []


def __appliquerGlueBord(image: PlayerImage, blocs_lines: LstLstBlocs, blocs_columns: LstLstBlocs) -> LstSuggestions:
    print("Fonction appliquerGlueBord manquante !")
    return []

def __appliquerBoucheTrou(image: PlayerImage, blocs_lines: LstLstBlocs, blocs_columns: LstLstBlocs) -> LstSuggestions:
    print("Fonction appliquerBoucheTrou manquante !")
    return []

def __plusDeMonoSuggestions(image: PlayerImage, blocs_lines: LstLstBlocs, blocs_columns: LstLstBlocs) -> LstSuggestions:
    print("Fonction plusDeMonoSuggestions manquante !")
    return []

def __plusDeSuggestions(image: PlayerImage, blocs_lines: LstLstBlocs, blocs_columns: LstLstBlocs) -> LstSuggestions:
    print("Fonction plusDeSuggestions manquante !")
    return []


def load_function(name: str) -> callable:
    if name in globals():
        return globals()[name]
    name = '__' + name
    if name not in globals():
        print(f"Implementation Error : {name} not defined")
        raise ModuleNotFoundError(name)
    return globals()[name]


class Controller:
    size: int # Taille du tableau
    win: "Nonogram" # Classe Nonogram
    array: list[list[int]] | None

    # Image pour le modèle
    modelImage: Image | None
    playerImage: Image | None

    # Blocs sur les lignes
    linesBlocs: LstLstBlocs | None
    viewLinesBlocs: list[list[tuple[int, int, bool]]]

    # Blocs sur les colonnes
    columnsBlocs: LstLstBlocs | None
    viewColumnsBlocs: list[list[tuple[int, int, bool]]]

    # Histogramme des couleurs
    nbPerColor: NbParCouleur | None

    def __init__(self):
        self.__error = None
        self.win = None
        self.size = 5
        self.array = None

        # Récupération des méthodes existantes
        # et remplacement par des méthodes par défaut si non existantes
        self.creerImage = load_function("creerImage")
        self.getBlocsLignes = load_function("getBlocsLignes")
        self.getBlocsColonnes = load_function("getBlocsColonnes")
        self.isVuCellJoueur = load_function("isVuCellJoueur")
        self.isCouleurCorrecteImage = load_function("isCouleurCorrecteImage")
        self.setCellImage = load_function("setCellImage")
        self.reinitialiserImage = load_function("reinitialiserImage")
        self.isVuImage = load_function("isVuImage")
        self.verifierBlocsLigneImage = load_function("verifierBlocsLigneImage")
        self.verifierBlocsColonneImage = load_function("verifierBlocsColonneImage")
        self.isLigneDecouverteImage = load_function("isLigneDecouverteImage")
        self.isColonneDecouverteImage = load_function("isColonneDecouverteImage")
        self.getCellsNonVuesLigneImage = load_function("getCellsNonVuesLigneImage")
        self.getCellsNonVuesColonneImage = load_function("getCellsNonVuesColonneImage")
        self.getNbParCouleur = load_function("getNbParCouleur")
        self.getCouleursVuImage = load_function("getCouleursVuImage")
        self.appliquerMonoRecouvrement = load_function("appliquerMonoRecouvrement")
        self.appliquerRecouvrement = load_function("appliquerRecouvrement")
        self.appliquerMonoGlueBord = load_function("appliquerMonoGlueBord")
        self.appliquerGlueBord = load_function("appliquerGlueBord")
        self.appliquerBoucheTrou = load_function("appliquerBoucheTrou")
        self.plusDeMonoSuggestions = load_function("plusDeMonoSuggestions")
        self.plusDeSuggestions = load_function("plusDeSuggestions")


        # self.initialise_boardgame()
        # self.initialize_scene1()


    def initialise_game(self, size: int, monochrome: bool) -> None:
        """
        Initialise le plateau de jeu

        :param size: Taille de l'image (nombre de lignes/colonnes)
        :param monochrome: Détermine si le jeu comporte des cellules de couleur ou non
        :return: Rien
        :raise ValueError: Si la configuration n'est pas reconnue
        """
        self.size = size
        # On commence par créer le tableau 2D
        self.array = get_test_image(self.size, monochrome)
        self.modelImage = self.creerImage(self.size, self.array)
        self.playerImage = self.creerImage(self.size)
        # Code théoriquement inutile, mais permettant de prendre en compte
        # le retour de la méthode creerImage
        self.array = [[0 if cell[VALEUR] is None else cell[VALEUR] for cell in line] for line in self.modelImage ]
        self.nbPerColor = None
        self.compute_lines_columns_blocs()

    def compute_lines_columns_blocs(self):
        self.linesBlocs = self.getBlocsLignes(self.modelImage)
        self.viewLinesBlocs = [[(bloc[NOMBRE], bloc[COULEUR], bloc[VU]) for bloc in lineBlocs] for lineBlocs in self.linesBlocs]
        self.columnsBlocs = self.getBlocsColonnes(self.modelImage)
        self.viewColumnsBlocs = [[(bloc[NOMBRE], bloc[COULEUR], bloc[VU]) for bloc in columnBlocs] for columnBlocs in self.columnsBlocs]
        self.nbPerColor = self.getNbParCouleur(self.size, self.linesBlocs)

    def get_image(self) -> list[list[int]]:
        return self.array

    def set_win(self, win: "Nonogram") -> None:
        self.win = win
        return None

    def is_ended(self) -> bool:
        return self.array is not None and self.isVuImage(self.playerImage)

    def get_size(self) -> int:
        return self.size

    def reset_image(self) -> None:
        self.reinitialiserImage(self.playerImage)
        self.compute_lines_columns_blocs()

    def get_blocs_line(self, li: int) -> list[tuple[int, int, bool]]:
        return self.viewLinesBlocs[li]

    def get_blocs_column(self, col: int) -> list[tuple[int, int, bool]]:
        return self.viewColumnsBlocs[col]

    def initialize_scene1(self):
        from View.Exemples import scene1, colors1
        self.array = []
        for line in scene1:
            _line = []
            for v in line:
                if v == 0:
                    _line.append(None)
                else:
                    _line.append(colors1[v])
            self.array.append(_line)

    def get_solved_colors(self) -> list[int]:
        # print("NbPerColors: ", self.nbPerColor)
        if self.nbPerColor is not None and len(self.nbPerColor) > 0:
            lst = self.getCouleursVuImage(self.playerImage, self.nbPerColor)
            # print("Solved colors:", lst)
            return lst
        # print("Cannot search solved colors")
        return []

    def get_mono_blocs_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.appliquerMonoRecouvrement(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_blocs_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.appliquerRecouvrement(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_mono_glue_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.appliquerMonoGlueBord(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_glue_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.appliquerGlueBord(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_empty_holes_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.appliquerBoucheTrou(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_more_mono_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.plusDeMonoSuggestions(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}

    def get_more_suggestions(self) -> dict[tuple[int, int], int]:
        lst = self.plusDeSuggestions(self.playerImage, self.linesBlocs, self.columnsBlocs)
        return {(d[POSITION][LIGNE], d[POSITION][COLONNE]): d[COULEUR] for d in lst}


    def mouse_clicked(self, coord: tuple[int, int], color: int, no_line_solve: bool = False, no_column_solve: bool = False,
                      recursive: int = 0) -> None:
        self.__error = False
        if recursive > 20:
            self.win.display_message("Une erreur de récursivité s'est produite ! \nVérifiez vos fonctions getCellsNonVuesLigne/ColonneImage")
            self.__error = True
            return None
        li, co = coord
        pos = {LIGNE: li, COLONNE: co}
        if not self.isVuCellJoueur(self.playerImage, pos):
            if not self.isCouleurCorrecteImage(self.modelImage, pos, color):
                self.win.set_cell_error(coord)
            self.win.set_cell_visible(coord)
            self.setCellImage(self.playerImage, pos, getCouleurCellule(getCellImage(self.modelImage, pos)))
            # Mise à jour des blocs de la ligne et de la colonne correspondantes
            if self.verifierBlocsLigneImage(self.playerImage, self.linesBlocs[li], li):
                self.win.update_digit_line(li, [b[VU] for b in self.linesBlocs[li]])
            if self.verifierBlocsColonneImage(self.playerImage, self.columnsBlocs[co], co):
                self.win.update_digit_column(co, [b[VU] for b in self.columnsBlocs[co]])
            # On vérifie si la ligne et la colonne correspondantes sont découvertes
            self.win.set_refresh(True)
            if not no_line_solve and self.isLigneDecouverteImage(self.playerImage, self.linesBlocs[li], li):
                columns = self.getCellsNonVuesLigneImage(self.playerImage, li)
                self.win.animate_line(li)
                for c in columns:
                    self.mouse_clicked((li, c), 0, True, no_column_solve, recursive + 1)
                    if self.__error:
                        return None
            if not no_column_solve and self.isColonneDecouverteImage(self.playerImage, self.columnsBlocs[co], co):
                lines = self.getCellsNonVuesColonneImage(self.playerImage, co)
                self.win.animate_column(co)
                for l in lines:
                    self.mouse_clicked((l, co), 0, no_line_solve, True, recursive + 1)
                    if self.__error:
                        return None
        else:
            print("Cellule déjà vue !")
        return None
