import pygame

from View.Consts import Consts
from View.Images import Images

class Lives:
    _hearts: pygame.Surface
    _dead_hearts: pygame.Surface
    _lives: int # Nombre total de vies
    _active_lives: int # Nombre de vies restantes
    _x: int # Abscisse de début des dessins
    _y: int # Ordonnée de début des dessins
    _width: int # Largeur pour le dessin d'un coeur
    _full_width: int # Largeur totale pour le dessin des coeurs
    _color: pygame.Color


    def __init__(self, lives: int, x: int, y: int, width: int, height: int):
        self._hearts = Images.img_heart
        self._dead_hearts = Images.img_dead_heart

        # Centrer les images sur la surface
        self._full_width = width
        self._width = (width - lives*self._hearts.get_width()) // (lives + 1)
        self._lives = lives
        self._active_lives = lives
        self._x = x
        self._y = (y + height - self._hearts.get_height()) // 2
        self._color = pygame.Color(255, 232, 198, Consts.Alpha)

    def reset_active_lives(self):
        self._active_lives = self._lives

    def decrease(self):
        if self._active_lives > 0:
            self._active_lives -= 1

    def get_active_lives(self):
        return self._active_lives

    def draw(self, screen: pygame.Surface):
        x = self._x
        pygame.draw.rect(screen, self._color, (x, self._y - Consts.Border,
                                               self._full_width, self._hearts.get_height() + 2 * Consts.Border),
                         border_radius=20)
        x += self._width
        for i in range(self._lives):
            if i < self._active_lives:
                screen.blit(self._hearts, (x, self._y))
            else:
                screen.blit(self._dead_hearts, (x, self._y))
            x += self._width + self._hearts.get_width()
