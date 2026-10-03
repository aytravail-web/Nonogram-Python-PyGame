import pygame

class Consts:
    """
    Intensité de la transparence
    """
    Alpha: int = 192
    """
    Couleur du trait entourant une cellule du tableau
    """
    RectLineColor: pygame.Color = pygame.Color(64, 64, 64)
    """
    Couleur du trait d'une cellule où se trouve la souris
    """
    SelectedRectLineColor: pygame.Color = pygame.Color(79, 164, 255)
    """
    Largeur du trait entourant une cellule du tableau où se trouve la souris
    """
    SelectedRectLineWidth: int = 3
    """
    Couleur de fond d'une cellule active (non découverte)
    """
    RectBackgroundColor: pygame.Color = pygame.Color(255, 242, 251, Alpha)
    """
    Largeur du trait d'une cellule du tableau
    """
    RectLineWidth: int = 1
    """
    Couleur du trait encadrant le tableau et des traits divisant le tableau en parts égales (2 ou 3)
    """
    BorderLineColor: pygame.Color = pygame.Color(10, 10, 10)
    """
    Largeur du trait encadrant le tableau...
    """
    BorderLineWidth: int = 3
    """
    Couleur de fond pour les chiffres
    """
    DigitFontSize: int = 30
    DigitBackground: pygame.Color = pygame.Color(170, 197, 255, Alpha)
    DigitRoundCorner: int = 5
    DigitHorizontalSpace: int = 10
    DigitVerticalSpace: int = 10
    DigitHorizontalSize: int = 300
    DigitVerticalSize: int = 300
    DigitBorder: int = 4

    Border: int = 10

    WindowWidth: int = 1024
    WindowHeight: int = 768