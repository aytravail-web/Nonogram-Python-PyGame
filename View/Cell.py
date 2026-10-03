import pygame

from View.Consts import Consts

"""
Classe représentant une cellule/case du tableau

Cette cellule doit pouvoir :

- Mémoriser si elle est active ou non.
- Répondre à un clic.
- Répondre à un survol de la souris au-dessus de cette dernière.
  Dans ce cas, elle doit être la dernière à être dessinée pour que ses bords mis en couleur soient
  dessinés au-dessus de ceux des cellules voisines, sauf si elle n'est plus active
- Savoir se dessiner à la bonne place.

"""
class Cell :
    _rect: pygame.Rect
    _is_solved: bool
    _is_error: bool
    _color: pygame.Color
    _is_mouse_over: bool

    def __init__(self, size: int, x: int, y: int, color: pygame.Color | None) -> None:
        self._rect = pygame.Rect(x, y, size, size)
        self._is_solved = False
        self._is_error = False
        self._color = color
        self._is_mouse_over = False

    def set_solved(self, active: bool) -> None:
        self._is_solved = active

    def get_solved(self) -> bool:
        return self._is_solved

    def get_color(self):
        return self._color

    def get_x(self) -> int:
        return self._rect.x

    def get_y(self) -> int:
        return self._rect.y

    def get_width(self) -> int:
        return self._rect.width

    def get_height(self) -> int:
        return self._rect.height

    def get_rect(self) -> pygame.Rect:
        return self._rect

    def set_mouse_over(self, active: bool) -> None:
        self._is_mouse_over = active

    def is_mouse_over(self) -> bool:
        return self._is_mouse_over

    def set_error(self, active: bool) -> None:
        self._is_error = active

    def is_error(self) -> bool:
        return self._is_error

    @staticmethod
    def draw_suggestion_cell(canvas: pygame.Surface, rect: pygame.Rect, color_index: int) -> None:
        color = pygame.Color(255, 215, 0)
        from View.ArrayCell import ArrayCell
        fill = ArrayCell.Colors[color_index]
        if fill is None:
            # Dessiner la croix
            pygame.draw.line(canvas, color, rect.topleft, rect.bottomright, Consts.BorderLineWidth)
            pygame.draw.line(canvas, color, rect.bottomleft, rect.topright, Consts.BorderLineWidth)
        else:
            canvas.fill(fill, rect)
        pygame.draw.rect(canvas, color, rect, 5)

    def draw(self, canvas: pygame.Surface, cheat_code: bool) -> None:
        if not self.get_solved() and not cheat_code:
            # Remplissage du rectangle
            # print(Consts.RectBackgroundColor)
            pygame.draw.rect(canvas, Consts.RectBackgroundColor, self._rect)
            # Contour du rectangle
            color = Consts.SelectedRectLineColor if self._is_mouse_over else Consts.RectLineColor
            width = Consts.SelectedRectLineWidth if self._is_mouse_over else Consts.RectLineWidth
            pygame.draw.rect(canvas, color, self._rect, width)
        else:
            color = pygame.Color(255, 101, 73) if self._is_error else Consts.RectLineColor
            if self._color is not None:
                pygame.draw.rect(canvas, self._color, self._rect)
                pygame.draw.rect(canvas, color, self._rect, Consts.RectLineWidth)
            else:
                # Dessiner une croix pour montrer une case vide.
                pygame.draw.rect(canvas, Consts.RectBackgroundColor, self._rect)
                pygame.draw.rect(canvas, color, self._rect, Consts.RectLineWidth)
                # Dessiner la croix
                pygame.draw.line(canvas, color, self._rect.topleft, self._rect.bottomright, Consts.BorderLineWidth)
                pygame.draw.line(canvas, color, self._rect.bottomleft, self._rect.topright, Consts.BorderLineWidth)

    def contains(self, pos: tuple[int, int]) -> bool:
        return self._rect.collidepoint(*pos)

    def clic(self, color: pygame.Color | None) -> bool:
        if self._is_solved:
            return True # Pas d'erreur
        self._is_error = color != self._color
        self._is_solved = True
        return not self._is_error