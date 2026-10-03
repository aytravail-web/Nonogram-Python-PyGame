# Model/CustomTypes.py

from typing import Union

# Définition des alias de types
# permettant une meilleure lisibilité du code

# Alias du type des cellules d'une image
Cellule = dict[str, Union[int, None]]

# Alias du type d'une image : tableau 2D carré (même nombre de lignes que de colonnes)
# rempli de cellules
Image = list[list[Cellule]]

# Images manipulées par le jeu, ne pouvant contenir que des entiers
ModelImage = list[list[dict[str, int]]]

# Images manipulées par le joueur, pouvant contenir outre des entiers, la valeur None
PlayerImage = list[list[dict[str, Union[int,None]]]]

# Alias du type d'une position
Position = dict[str, int]

# Alias du type Bloc
Bloc = dict[str, Union[int, bool]]

# Liste de blocs
LstBlocs = list[Bloc]

# Liste de listes de blocs
LstLstBlocs = list[LstBlocs]

# Liste de couleurs
LstCouleurs = list[int]

# Dictionnaire associant à chaque couleur le nombre de cellules ayant cette couleur
NbParCouleur = dict[int, int]

# Suggestions de coups à jouer modélisés par un dictionnaire à deux clés :
# - POSITION : Position dans l'image
# - COULEUR : Couleur à placer (la couleur transparente, 0, étant acceptée)
Suggestion = dict[str, Union[Position,int]]

# Liste de suggestions
LstSuggestions = list[Suggestion]

# Rangée d'une image : ligne ou colonne
Rangee = list[Cellule]

# Liste des indices avec leur couleur sous forme de tuple
LstIndexCouleurs = list[tuple[int, int]]
