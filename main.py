import pygame
from View.Nonogram import Nonogram
from Controller.Controller import Controller

# Essais graphiques
#



# Calcul de la taille de la fenêtre
# Nombre de cellules
controller = Controller()


nonogram = Nonogram(controller)

nonogram.play()


