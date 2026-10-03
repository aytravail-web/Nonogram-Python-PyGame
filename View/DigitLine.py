import pygame
from View.Consts import Consts

class DigitLine:
    _x: int
    _y: int
    _width: int
    _height: int
    _digits: list[tuple[str, pygame.Color, bool]] # booléen : True = actif, False = inactif
    _digit_width: int
    _font: pygame.font.Font
    _text: pygame.Surface
    _h_space: int
    _font_size: int
    _mono: bool # Détermine si le jeu est zen monochrome ou en couleur

    def __init__(self, digits: list[tuple[int, pygame.Color, bool]], x: int, y: int, width: int, height: int, monochrome: bool = True):
        # On convertit les entiers en chaîne de caractères
        self._digits = [ (str(i), col, b) for i, col, b in digits]
        # On cherche la taille de la fonte pour que la chaîne tienne dans l'espace donné
        self._font_size = Consts.DigitFontSize
        pix_marge = 4 # On donne une marge de 2 pixels sur les dimensions
        font = pygame.sysfont.SysFont('Arial', self._font_size)
        w = 0
        h = 0
        for s, *_ in self._digits:
            (_w, _h) = font.size(s)
            w += Consts.DigitHorizontalSpace + _w
            h = max(h, _h)
        while (w > width - pix_marge or h > height - pix_marge) and self._font_size > 4:
            self._font_size -= 1
            font = pygame.sysfont.SysFont('Arial', self._font_size)
            w = 0
            h = 0
            for s, *_ in self._digits:
                (_w, _h) = font.size(s)
                w += Consts.DigitHorizontalSpace + _w
                h = max(h, _h)
        self._font = font
        if h < height:
            self._h_space = (height - h) // 2
        else:
            self._h_space = 0
        self._x = x
        self._y = y
        self._height = height
        self._mono = monochrome
        self._digit_width = Consts.DigitHorizontalSpace - Consts.DigitBorder

    def get_font_size(self) -> int:
        return self._font_size

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
        pygame.draw.rect(canvas, Consts.DigitBackground, (self._x, self._y + Consts.DigitBorder // 2,
                                                          Consts.DigitHorizontalSize, self._height - Consts.DigitBorder),
                         0, Consts.DigitRoundCorner)
        x = self._x + Consts.DigitHorizontalSize - Consts.Border
        y = self._y + self._h_space
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
            x -= _text.get_width()
            if not self._mono:
                r = _text.get_rect()
                r.move_ip(x - self._digit_width // 2, y)
                r.width += self._digit_width
                pygame.draw.rect(canvas, col, r, 0)
            canvas.blit(_text, (x, y))
            x -= Consts.DigitHorizontalSpace


