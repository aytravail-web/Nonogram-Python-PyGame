# tests/TestNonogram.py
import unittest

from random import randint, choice
from Model.Image import *
from Model.Bloc import *
from Model.Nonogram import *
from Model.Data import get_test_image
from Model.Joueur import *



class TestNonogram(unittest.TestCase):

    @unittest.skipIf('compterBlocsSurLigne' not in globals(), "compterBlocsSurLigne non écrite")
    def test_compterBlocsSurligne(self):
        for _ in range(100):
            image = get_test_image()
            img = creerImage(len(image), image)
            for i in range(len(image)):
                blocs = compterBlocsSurLigne(img, i)
                idx = 0
                # Vérification des blocs
                for num, bloc in enumerate(blocs):
                    n = bloc[NOMBRE]
                    c = bloc[COULEUR]
                    while idx < len(image) and image[i][idx] == 0:
                        idx += 1
                    cpt = 0
                    while idx < len(image) and image[i][idx] == c:
                        cpt += 1
                        idx += 1
                    self.assertEqual(cpt, n, f"Sur la ligne {image[i]}, le bloc {bloc} en position {num} (à partir de 0) ne correspond pas")

    @unittest.skipIf('compterBlocsSurLigne' not in globals(), "compterBlocsSurLigne non écrite")
    def test_QUALITE_compterBlocsSurligne(self):
        self.assertRaises(AssertionError, compterBlocsSurLigne, "image", 1)
        image = get_test_image()
        img = creerImage(len(image), image)
        self.assertRaises(AssertionError, compterBlocsSurLigne, img, "1")

    @unittest.skipIf('compterBlocsSurColonne' not in globals(), "compterBlocsSurColonne non écrite")
    def test_compterBlocsSurColonne(self):
        for _ in range(100):
            image = get_test_image()
            img = creerImage(len(image), image)
            for co in range(len(image)):
                blocs = compterBlocsSurColonne(img, co)
                idx = 0
                # Vérification des blocs
                for num, bloc in enumerate(blocs):
                    n = bloc[NOMBRE]
                    c = bloc[COULEUR]
                    while idx < len(image) and image[idx][co] == 0:
                        idx += 1
                    cpt = 0
                    while idx < len(image) and image[idx][co] == c:
                        cpt += 1
                        idx += 1
                    self.assertEqual(cpt, n, f"Sur la colonne {[image[i][co] for i in range(len(image))]}, le bloc {bloc} en position {num} (à partir de 0) ne correspond pas")

    @unittest.skipIf('compterBlocsSurColonne' not in globals(), "compterBlocsSurColonne non écrite")
    def test_QUALITE_compterBlocsSurColonne(self):
        self.assertRaises(AssertionError, compterBlocsSurColonne, "image", 1)
        image = get_test_image()
        img = creerImage(len(image), image)
        self.assertRaises(AssertionError, compterBlocsSurColonne, img, "1")

    @unittest.skipIf('isCouleurCorrecteImage' not in globals(), "isCouleurCorrecteImage non écrite")
    def test_isCouleurCorrecteImage(self):
        colors = get_test_image(10)
        image = creerImage(len(colors), colors)
        for i in range(len(colors)):
            for j in range(len(colors)):
                pos = {LIGNE: i, COLONNE: j}
                self.assertTrue(isCouleurCorrecteImage(image, pos, colors[i][j]))
                self.assertFalse(isCouleurCorrecteImage(image, pos, colors[i][j] + 1))

    @unittest.skipIf('isVuCellJoueur' not in globals(), "isVuCellJoueur non écrite")
    def test_isVuCellJoueur(self):
        size = 10
        image = creerImage(size)
        for i in range(size):
            for j in range(size):
                pos = {LIGNE: i, COLONNE: j}
                self.assertFalse(isVuCellJoueur(image, pos))
                image[i][j][VALEUR] = randint(0, 5)
                self.assertTrue(isVuCellJoueur(image, pos))

    @unittest.skipIf('isLigneDecouverteImage' not in globals(), "isLigneDecouverte non écrite")
    def test_isLigneDecouverteImage(self):
        img = [ [ 1, 0, 0, 0, 2],
                [ 2, 0, 0, 0, 1],
                [ 3, 0, 0, 0, 0],
                [ 4, 0, 0, 0, 0],
                [ 5, 0, 0, 0, 0],]
        image_player = creerImage(len(img))
        image = creerImage(len(img), img)
        bloc = compterBlocsSurLigne(image, 0)
        image_player[0][0][VALEUR] = 1
        image_player[0][4][VALEUR] = 2
        image_player[1][0][VALEUR] = 2
        image_player[1][4][VALEUR] = 1
        bloc = compterBlocsSurLigne(image, 0)
        self.assertTrue(isLigneDecouverteImage(image_player, bloc, 0),
                        f"Erreur sur la fonction isLigneDecouverteImage: bloc={bloc}, ligne={image_player[0]}")
        bloc = compterBlocsSurLigne(image, 1)
        self.assertTrue(isLigneDecouverteImage(image_player, bloc, 1),
                        f"Erreur sur la fonction isLigneDecouverteImage: bloc={bloc}, ligne={image_player[1]}")
        bloc = compterBlocsSurLigne(image, 2)
        self.assertFalse(isLigneDecouverteImage(image_player, bloc, 2),
                         f"Erreur sur la fonction isLigneDecouverteImage: bloc={bloc}, ligne={image_player[2]}")
        bloc = compterBlocsSurColonne(image, 1)
        self.assertTrue(isColonneDecouverteImage(image_player, bloc, 1))

    @unittest.skipIf('getNbParCouleur' not in globals(), "Fonction getNbParCouleur non écrite")
    def test_getNbParCouleur(self):
        for _ in range(100):
            img = get_test_image()
            image = creerImage(len(img), img)
            line_blocs = getBlocsLignes(image)
            column_blocs = getBlocsColonnes(image)
            h1 = getNbParCouleur(len(img), line_blocs)
            h2 = getNbParCouleur(len(img), column_blocs)
            self.assertEqual(h1, h2, f"Problème dans le décompte des couleurs : h1={h1}, h2={h2}")

    @unittest.skipIf('getCouleursVuImage' not in globals(), "Fonction getCouleursVuImage non écrite")
    def test_getCouleursVuImage(self):
        for _ in range(10):
            img = get_test_image()
            model_image = creerImage(len(img), img)
            player_image = creerImage(len(img))
            line_blocs = getBlocsLignes(model_image)
            histo = getNbParCouleur(len(img), line_blocs)
            colors = list(range(len(histo)))
            self.assertEqual(set(), set(getCouleursVuImage(player_image, histo)), "Aucune couleur ne devrait être vu")
            # Découvrir aléatoirement les couleurs
            solved_colors = set()
            while len(colors) > 0:
                col = choice(colors)
                colors.remove(col)
                for i in range(len(model_image)):
                    for j in range(len(model_image)):
                        if model_image[i][j][VALEUR] == col:
                            player_image[i][j][VALEUR] = col
                solved_colors.add(col)
                self.assertEqual(solved_colors, set(getCouleursVuImage(player_image, histo)), f"Erreur avec {histo}")


