# Model/Data.py

from random import randint

# Simule des images aléatoirement

def get_test_image(dim: int = 15, monochrome: bool = False) -> list[list[int]]:
    """
    Retourne un tableau carré d'entiers choisis aléatoirement dans l'intervalle [0, n] où 1 <= n <= 5.

    Deux cellules voisines ont 66 % de chance d'avoir la même couleur...

    :return: Image simulée
    """
    color_max = randint(2, 5) if not monochrome else 1
    image = []
    # Génération de la première ligne
    ligne = [randint(0, color_max)]
    for i in range(1, dim):
        val = randint(0, color_max)
        ok = val == ligne[i - 1] or randint(0, 2) == 2
        while not ok:
            val = randint(0, color_max)
            ok = val == ligne[i - 1] or randint(0, 2) == 2
        ligne.append(val)
    image.append(ligne)
    # Génération des autres lignes
    for i in range(1, dim):
        ligne = []
        val = randint(0, color_max)
        ok = val == image[i - 1][0] or randint(0, 2) == 2
        while not ok:
            val = randint(0, color_max)
            ok = val == image[i - 1][0] or randint(0, 2) == 2
        ligne.append(val)
        for j in range(1, dim):
            val = randint(0, color_max)
            ok = val == image[i - 1][j] or val == ligne[j - 1] or randint(0, 2) == 2
            while not ok:
                val = randint(0, color_max)
                ok = val == image[i - 1][j] or val == ligne[j - 1] or randint(0, 2) == 2
            ligne.append(val)
        image.append(ligne)
    return image

def initialise_monochrome_image(size: int = 15) -> list[list[int]]:
    """
    Initialise le plateau de jeu

    :return: Rien
    :raise ValueError: Si la configuration n'est pas reconnue
    """
    # On commence par créer le tableau 2D
    array = list()
    for _ in range(size):
        array.append([0] * size)

    # print("Nombre de lignes : ", len(self.array))
    # for line in self.array:
    #     print("Nombre de cases dans la ligne : ", len(line))

    # Remplissage aléatoire de 60 % des rectangles
    nb = size * size * 0.6
    while nb > 0:
        i = randint(0, size - 1)
        j = randint(0, size - 1)
        if array[i][j] == 0:
            # On cherche à placer les carrés ensemble
            ok = False
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if 0 <= ii < size and 0 <= jj < size and array[ii][jj] != 0:
                        ok = True
                        break
                if ok:
                    break
            if ok or randint(0, 4) == 3:
                array[i][j] = 1
                nb -= 1
    return array

