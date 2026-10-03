import pygame
from View.Consts import Consts

class DigitColumn:
    _x: int
    _y: int
    _width: int
    _height: int
    _digits: list[tuple[str, pygame.Color, bool]] # booléen : True = actif, False = inactif
    _digit_height: int
    _digit_width: int
    _font: pygame.font.Font
    _v_space: int
    _mono: bool # Détermine si le jeu est zen monochrome ou en couleur

    def __init__(self, digits: list[tuple[int, pygame.Color, bool]], x: int, y: int, width: int, height: int,
                 monochrome: bool = True, font_size: int = Consts.DigitFontSize):
        # On convertit les entiers en chaîne de caractères
        self._digits = [ (str(i), col, b) for i, col, b in digits]
        # On cherche la taille de la fonte pour que la chaîne tienne dans l'espace donné
        size = font_size
        pix_marge = 4 # On donne une marge de 2 pixels sur les dimensions
        font = pygame.sysfont.SysFont('Arial', size)
        w = 0
        h = 0
        for s, *_ in self._digits:
            (_w, _h) = font.size(s)
            w = max(w, _w)
            h += _h + Consts.DigitVerticalSpace
        while (w > width - pix_marge or h > height - pix_marge) and size > 4:
            size -= 1
            font = pygame.sysfont.SysFont('Arial', size)
            w = 0
            h = 0
            for s, *_ in self._digits:
                (_w, _h) = font.size(s)
                w = max(w, _w)
                h += _h + Consts.DigitVerticalSpace
        self._font = font
        if w < width:
            self._w_space = (width - w) // 2
        else:
            self._w_space = 0
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._mono = monochrome
        self._digit_height = Consts.DigitVerticalSpace - Consts.DigitBorder
        self._digit_width = width - 2*Consts.DigitBorder

    def update_blocs(self, vus: list[bool]) -> None:
        """
        Permet de mettre à jour le booléen vu des tuples
        :param vus: Liste de booléens correspondant à l'état vu des blocs
        :return:
        """
        for i in range(len(self._digits)):
            if self._digits[i][2] != vus[i]:
                self._digits[i] = (self._digits[i][0], self._digits[i][1], vus[i])

    def draw(self, canvas: pygame.Surface):
        pygame.draw.rect(canvas, Consts.DigitBackground, (self._x + Consts.DigitBorder // 2, self._y,
                                                          self._width - Consts.DigitBorder, Consts.DigitVerticalSize),
                         0, Consts.DigitRoundCorner)
        x = self._x + self._w_space
        xr = self._x + Consts.DigitBorder
        y = self._y + Consts.DigitVerticalSize - Consts.DigitBorder
        color = pygame.Color(0, 0, 0) if self._mono else pygame.Color(255, 255, 255)
        unabled_color = pygame.Color(128, 128, 128)
        for s, col, active in reversed(self._digits):
            if active:
                col = pygame.Color(col)
                col.a = 64
                t_color = unabled_color
            else:
                t_color = color
            _text = self._font.render(s, True, t_color)
            if not self._mono:
                r = _text.get_rect()
                r.move_ip(x + Consts.DigitBorder // 2, y + Consts.DigitBorder // 2)
                r.width = self._width - Consts.DigitBorder
                r.height += (Consts.DigitVerticalSpace - Consts.DigitBorder)
                r = pygame.Rect((xr, y - _text.get_height() - Consts.DigitVerticalSpace + Consts.DigitBorder // 2),
                                (self._width - Consts.Border, Consts.DigitVerticalSpace + _text.get_height() - Consts.DigitBorder))
                pygame.draw.rect(canvas, col, r, 0)
            canvas.blit(_text, (x, y - _text.get_height() - Consts.DigitBorder))
            y -= (_text.get_height() + Consts.DigitVerticalSpace)


