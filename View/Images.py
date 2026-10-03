import pygame
from View.Consts import Consts

# Partie chargement des images
# Récupération des images du fond, des billes et des vides/trous
# ==============================================================


class Images:
    # Image de fond de l'écran
    img_background: pygame.Surface | None = None

    img_heart: pygame.Surface | None = None
    img_dead_heart: pygame.Surface | None = None


    # !! La base du trou doit être alignée avec la base des billes
    # Répertoire où se trouvent les images
    sources = 'Images/'

    # Largeur de la fenêtre
    w_width = Consts.WindowWidth
    # Hauteur de la fenêtre
    w_height = Consts.WindowHeight

    # Image utilisée pour l'icône
    caption = None

    @staticmethod
    def load_images():
        """
        Chargement des images du jeu

        :return: Rien
        :rtype: None
        """
        # Chargement des images
        # ---------------------
        Images.img_background = pygame.image.load(Images.sources + 'fond2.png')
        Images.img_heart = pygame.image.load(Images.sources + 'coeur_s.png')
        Images.img_dead_heart = pygame.image.load(Images.sources + 'coeur_bleu_s.png')

        # Icône du jeu
        Images.caption = pygame.image.load(Images.sources + 'caption.png')

    @staticmethod
    def convert(screen: pygame.Surface) -> None:
        Images.img_background = Images.img_background.convert(screen)
        Images.img_heart = Images.img_heart.convert_alpha(screen)
        Images.img_dead_heart = Images.img_dead_heart.convert_alpha(screen)
        Images.caption = Images.caption.convert(screen)

    @staticmethod
    def get_window_size() -> tuple[int, int]:
        """
        Retourne la taille de la fenêtre principale.
        Il s'agit en fait des dimensions de l'image dessinée en fond d'écran.

        :return: (largeur, hauteur) de l'image
        :rtype: tuple[int, int]
        """
        return Images.w_width, Images.w_height

    @staticmethod
    def get_window_width() -> int:
        """
        Retourne la largeur de la fenêtre principale.
        Elle correspond à la largeur de l'image dessinée en fond d'écran.

        :return: Largeur de la fenêtre principale
        :rtype: int
        """
        return Images.w_width

    @staticmethod
    def get_window_height() -> int:
        """
        Retourne la hauteur de la fenêtre principale.
        Elle correspond à la hauteur de l'image dessinée en fond d'écran.

        :return: Hauteur de la fenêtre principale
        :rtype: int
        """
        return Images.w_height





