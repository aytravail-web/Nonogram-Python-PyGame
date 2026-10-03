import pygame

from Controller import Controller
from View.Consts import Consts
from View.Cell import Cell
from View.DigitLine import DigitLine
from View.DigitColumn import DigitColumn
from View.Lives import Lives

class ArrayCell:
    # Tableau 2D des cellules graphiques
    _cells: list[list[Cell]]
    # Cellule au-dessus de laquelle se trouve la souris
    _selected_cell: Cell | None
    # Position [ligne, colonne] de la cellule au-dessus de laquelle se trouve la souris
    _selected_cell_pos: tuple[int, int] | None
    # Lignes dessinant le quadrillage complet du jeu
    _lines: list[list[tuple[int, int]]] # Utilisées pour le quadrillage
    # Liste des objets gérant l'affichage du nombre de couleurs dans la ligne
    _digit_lines: list[DigitLine] # Liste des lignes contenant le nombre de blocs de même couleur dans les lignes
    # Liste des objets gérant l'affichage du nombre de couleurs dans la colonne
    _digit_columns: list[DigitColumn] # Liste des colonnes contenant le nombre de blocs de même couleur dans les colonnes
    # Coordonnées du coin supérieur de l'affichage (redondant avec l'attribut _content_rect
    _left_corner: tuple[int, int]
    # Taille d'une cellule (carrée)
    _size: int
    # Nombre de lignes (= nombre de colonnes)
    _nb: int
    # Rectangle englobant l'affichage du tableau
    _content_rect: pygame.Rect # Rectangle contenant le dessin de la grille
    # Affichage/Gestion des vies
    _lives: Lives
    # Largeur du tableau des cellules
    _width: int
    # Permet de déterminer s'il y a des couleurs ou si c'est monochrome
    _monochrome: bool
    # Controller
    _controller: Controller

    # Suggestions
    _suggestions: dict[tuple[int, int], int] | None

    # Palette de couleurs
    _palette: list[pygame.Color] | None

    # Palette de couleurs par défaut
    Colors = [
        None,
        pygame.Color(10, 10, 10), # Black
        pygame.Color(128, 128, 128), # Gray
        pygame.Color(255, 20, 147), # DeepPink
        pygame.Color(178, 34, 34), # Firebrick
        pygame.Color(255, 140, 0), # DarkOrange
        pygame.Color(160, 82, 45), # Sienna
        pygame.Color(0, 139, 139), # DarkCyan
        pygame.Color(25, 25, 112), # MidnightBlue
        pygame.Color(30, 144, 255), # DodgerBlue
        pygame.Color(34, 139, 34), # ForestGreen
    ]


    def __init__(self, controller: Controller, nb: int, x: int, y: int, size: int, colors: list[list[int]], lives: Lives) -> None:
        """
        Crée un tableau carré de nb x nb cellules de taille size x size

        :param controller: Contrôleur
        :param nb: Nombre de lignes et de colonnes du tableau
        :param x: Position en abscisse du tableau
        :param y: Position en ordonnée du tableau
        :param size: Taille d'une cellule
        :param colors: Tableau 2D des couleurs à afficher ??
        :param lives: Classe gérant les vies du jeu
        """
        self._controller = controller
        self._left_corner = (x, y)
        self._size = size
        self._nb = nb
        self._cells = []
        self._lives = lives
        self._suggestions = {}
        # self._monochrome = True
        print("Taille du tableau : ", nb, "x", nb, " = ", nb * nb, " cases")
        _cc = set()
        for i in range(nb):
            _line = []
            for j in range(nb):
                # print(f"({i}, {j}")
                _line.append(Cell(size, x + j * size, y + i * size, ArrayCell.Colors[colors[i][j]]))
                _cc.add(colors[i][j])
            self._cells.append(_line)
        self._selected_cell = None
        __nb = len(_cc)
        self._monochrome = len(_cc) == 2
        self._palette = ArrayCell.Colors[0:__nb]
        # Création des lignes de bord et de partage de grille
        # Cadre autour
        self._lines = list()
        dim = nb * size
        self._lines.append([(x, y), (x + dim, y)]) # Bord vertical gauche
        self._lines.append([(x, y + dim), (x + dim, y + dim)]) # Bord vertical droit
        self._lines.append([(x, y), (x, y + dim)]) # Bord horizontal haut
        self._lines.append([(x + dim, y), (x + dim, y + dim)]) # Bord horizontal bas
        self._width = dim
        self._content_rect = pygame.Rect(self._left_corner[0], self._left_corner[1], self._width, self._width)
        # Lignes séparatrices
        if nb % 3 == 0:
            step = nb // 3 * size
            for i in range(1, 3):
                self._lines.append([(x + i*step, y), (x + i*step, y + dim)])
                self._lines.append([(x, y + i*step), (x + dim, y + i*step)])
        elif nb % 2 == 0:
            step = nb // 2 * size
            self._lines.append([(x + step, y), (x + step, y + dim)])
            self._lines.append([(x, y + step), (x + dim, y + step)])
        self._digit_lines = []
        self._digit_columns = []
        font_size = self._init_digit_lines()
        self._init_digit_columns(font_size)

    def reset_image(self):
        """
        Réinitialise l'image en rendant toutes les cellules non résolues.

        :return:
        """
        vus = [False]*self._nb
        for i, lines in enumerate(self._cells):
            for cell in lines:
                cell.set_solved(False)
                cell.set_error(False)
            self.update_digit_line(i, vus)
            self.update_digit_column(i, vus)

    def get_colors(self) -> list[pygame.Color]:
        return self._palette

    def get_x(self) -> int:
        return  self._left_corner[0]

    def get_y(self) -> int:
        return self._left_corner[1]

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._width

    def get_rect_cell(self, li: int, co: int) -> pygame.Rect:
        return self._cells[li][co].get_rect()

    def set_suggestions(self, suggestions: dict[tuple[int, int], int]) -> None:
        self._suggestions = suggestions

    def update_digit_line(self, li: int, vus: list[bool]):
        """
        Met à jour l'état découvert des blocs de la ligne li
        :param li: Numéro de ligne commençant à 0
        :param vus: Liste des états découverts de chaque bloc
        :return:
        """
        self._digit_lines[li].update_blocs(vus)

    def update_digit_column(self, co: int, vus: list[bool]):
        """
        Met à jour l'état découvert des blocs de la ligne li
        :param co: Numéro de colonne commençant à 0
        :param vus: Liste des états découverts de chaque bloc
        :return:
        """
        self._digit_columns[co].update_blocs(vus)

    def draw(self, canvas: pygame.Surface, cheat_code: bool) -> None:
        for i, line in enumerate(self._cells):
            for j, cell in enumerate(line):
                if (i, j) in self._suggestions:
                    Cell.draw_suggestion_cell(canvas, cell.get_rect(), self._suggestions[(i, j)])
                elif cell == self._selected_cell:
                    continue
                else:
                    cell.draw(canvas, cheat_code)
        for line in self._lines:
            pygame.draw.line(canvas, Consts.BorderLineColor, line[0], line[1], Consts.BorderLineWidth)
        if self._selected_cell:
            self._selected_cell.draw(canvas, cheat_code)
        for _digit_line in self._digit_lines:
            _digit_line.draw(canvas)
        for _digit_column in self._digit_columns:
            _digit_column.draw(canvas)

    def _init_digit_lines(self) -> int:
        """
        Calcule les blocs de couleurs dans chaque ligne

        :return: Taille de la fonte calculée pour les lignes.
        """
        # On calcule les chiffres à afficher
        self._digit_lines.clear()
        y = self._left_corner[1]
        font_size = 0
        for li in range(len(self._cells)):
            blocs = self._controller.get_blocs_line(li)
            _nb = [(nb, ArrayCell.Colors[co], view) for nb, co, view in blocs]
            self._digit_lines.append(DigitLine(_nb, self._left_corner[0] - Consts.DigitHorizontalSize - Consts.Border,
                                               y, Consts.DigitHorizontalSize,
                                               self._size, self._monochrome))
            font_size = max(font_size, self._digit_lines[-1].get_font_size())
            y += self._size
        return font_size

    def _init_digit_columns(self, font_size: int):
        # On calcule les chiffres à afficher sur les colonnes
        self._digit_columns.clear()
        x = self._left_corner[0]
        y = self._left_corner[1] - Consts.Border - Consts.DigitVerticalSize
        for co in range(len(self._cells)):
            blocs = self._controller.get_blocs_column(co)
            _nb = [(nb, ArrayCell.Colors[co], view) for nb, co, view in blocs]
            self._digit_columns.append(DigitColumn(_nb, x,
                                               y, self._size, Consts.DigitVerticalSize,
                                                   font_size = font_size,
                                                   monochrome = self._monochrome))
            x += self._size

    def mouse_moved(self, pos: tuple[int, int]) -> bool:
        if self._content_rect.collidepoint(pos[0], pos[1]):
            # Détermination de la cellule contenant la souris
            _li: int = (pos[1] - self._left_corner[1]) // self._size
            _co: int = (pos[0] - self._left_corner[0]) // self._size
            if not self._cells[_li][_co].get_solved():
                if self._cells[_li][_co] == self._selected_cell:
                    return False
                if self._selected_cell is not None:
                    self._selected_cell.set_mouse_over(False)
                self._selected_cell = self._cells[_li][_co]
                self._selected_cell_pos = (_li, _co)
                self._selected_cell.set_mouse_over(True)
                return True
            elif self._selected_cell is not None:
                self._selected_cell.set_mouse_over(False)
                self._selected_cell = None
                return True
        elif self._selected_cell is not None:
            self._selected_cell.set_mouse_over(False)
            self._selected_cell = None
            return True
        return False

    def set_cell_error(self, pos: tuple[int, int]) -> None:
        if self._selected_cell is not None:
            self._selected_cell.set_mouse_over(False)
            self._selected_cell = None
        li, co = pos
        self._cells[li][co].set_error(True)
        self._lives.decrease()

    def set_cell_visible(self, pos: tuple[int, int]) -> None:
        if self._selected_cell is not None:
            self._selected_cell.set_mouse_over(False)
            self._selected_cell = None
        li, co = pos
        self._cells[li][co].set_solved(True)

    def mouse_clicked(self, pos: tuple[int, int]) -> tuple[int, int] | None:
        if self._content_rect.collidepoint(pos[0], pos[1]) and self._selected_cell is not None:
            return self._selected_cell_pos
        return None


    def get_rect(self) -> pygame.Rect:
        return self._content_rect