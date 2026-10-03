import pygame
from View.Cell import Cell
from View.Consts import Consts

class ColorSelection:
    _colors: list[Cell]
    _solved_colors: set
    _selection: int # Indice de la couleur sélectionnée dans le tableau _colors
    _x: int
    _y: int
    _width: int
    _height: int
    _color: pygame.Color # Couleur de fond
    _selected_color: pygame.Color # Couleur de fond de la couleur sélectionnée
    _content_rect: pygame.Rect

    def __init__(self, colors: list[pygame.Color], x: int, y: int, width:int, height: int):
        n = len(colors)
        # Définition de la largeur :
        _x = x
        b = 2*Consts.Border
        w = min(64, width - 2 * b)
        h = min(64, (height - (2 + n - 1) * b) // n)
        if h < w:
            w = h
        _height = w * n + (2 + n - 1) * b
        if _height < height:
            y += (height - _height ) // 2
        _y = y
        # Création des cellules
        self._colors = []
        x = _x + b
        y = _y + b
        for col in colors:
            self._colors.append(Cell(w, x, y, col))
            self._colors[-1].set_solved(True)
            y += w + b
        self._solved_colors = set()
        self._selection = 0
        _width = w + 2 * b
        self._content_rect = pygame.Rect(_x, _y, _width, _height)

        self._color = pygame.Color(84, 92, 255, Consts.Alpha)
        self._selected_color = pygame.Color(255, 95, 50, 255)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, self._content_rect,
                         border_radius=20)
        b = Consts.Border * 2
        solved_color = pygame.Color(0, 0, 0, 0)
        for i in range(len(self._colors)):
            cell = self._colors[i]
            if i in self._solved_colors:
                screen.fill(solved_color, cell.get_rect())
            else:
                if i == self._selection:
                    pygame.draw.rect(screen, self._selected_color, (cell.get_x() - Consts.Border,
                                                                    cell.get_y() - Consts.Border,
                                                                    cell.get_width() + b,
                                                                    cell.get_height() + b),
                                     border_radius=10)
                cell.draw(screen, True)
            # print("Couleur :", cell.get_color(), "Selected :", i == self._selection)

    def contains(self, pos: tuple[int, int]) -> bool:
        return self._content_rect.collidepoint(*pos)

    def update_solved_colors(self, colors: list[int]):
        # print("Updating solved colors with", colors)
        self._solved_colors |= set(colors)
        if self._selection in self._solved_colors:
            if not self.increase():
                self.decrease()


    def mouse_clicked(self, pos: tuple[int, int]) -> bool:
        """
        Traite le clic de la souris

        :param pos: Position de la souris
        :return: True si l'événement nécessite la mise à jour de l'affichage, False sinon
        """
        if not self._content_rect.collidepoint(*pos):
            return False
        for i in range(len(self._colors)):
            if i not in self._solved_colors and self._colors[i].contains(pos):
                if i != self._selection:
                    self._selection = i
                    return True
                return False
        return False

    def get_selected_color(self) -> pygame.Color:
        return self._colors[self._selection].get_color()

    def get_selected_color_index(self) -> int:
        return self._selection

    def increase(self) -> bool:
        mem = self._selection + 1
        while mem in self._solved_colors and mem < len(self._colors):
            mem += 1
        if mem < len(self._colors):
            self._selection = mem
            return True
        return False

    def decrease(self) -> bool:
        mem = self._selection - 1
        while mem in self._solved_colors and mem >= 0:
            mem -= 1
        if mem >= 0:
            self._selection = mem
            return True
        return False
