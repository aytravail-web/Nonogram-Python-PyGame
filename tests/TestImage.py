import unittest

from random import randint
from Model.Image import *



class TestImage(unittest.TestCase):
    @unittest.skipIf('creerImage' not in globals(), "creerImage non écrite")
    def test_creerImage(self):
        for i in range(5, 21):
            img = creerImage(i)
            self.assertTrue(type_image_full(img), "L'objet retourné ne correspond pas à une image")
            self.assertEqual(i, len(img), "La dimension de l'image retournée n'est pas correcte")
            for line in img:
                for cell in line:
                    self.assertIsNone(cell[VALEUR], "Les cellules de l'image doivent contenir None par défaut")
            # Création d'un tableau par défaut
            tab = [[randint(0, 4) for _ in range(i)] for _ in range(i)]
            img = creerImage(i, tab)
            self.assertTrue(type_image_full(img), "L'objet retourné ne correspond pas à une image")
            self.assertEqual(i, len(img), "La dimension de l'image retournée n'est pas correcte")
            for i, line in enumerate(img):
                for j, cell in enumerate(line):
                    self.assertEqual(tab[i][j], cell[VALEUR], "Initialisation avec tableau : Les cellules de l'image ne sont pas correctes")

    @unittest.skipIf('creerImage' not in globals(), "creerImage non écrite")
    def test_QUALITE_creerImage_raise_AssertionError(self):
        self.assertRaises(AssertionError, creerImage, "blablea")
        for i in range(-10, 5):
            self.assertRaises(AssertionError, creerImage, i)
        for i in range(21, 40):
            self.assertRaises(AssertionError, creerImage, i)
        tab = [[0]*10]*11
        self.assertRaises(AssertionError, creerImage, 11, tab)
        self.assertRaises(AssertionError, creerImage, 10, tab)
        tab = [[0]*8]*8
        for i in range(5, 21):
            if i == 8:
                continue
            self.assertRaises(AssertionError, creerImage, i, tab)

    @unittest.skipIf('getCellImage' not in globals(),
                     "getCellImage non écrit")
    def test_getCellImage(self):
        for _ in range(5):
            for n in range(5, 21):
                img = creerImage(n)
                for i, line in enumerate(img):
                    for j, cell in enumerate(line):
                        self.assertIsNone(getCellImage(img, {LIGNE: i, COLONNE: j})[VALEUR])
                tab = [[randint(0, 4) for _ in range(n)] for __ in range(n)]
                img = creerImage(n, tab)
                for i, line in enumerate(img):
                    for j, cell in enumerate(line):
                        self.assertEqual(tab[i][j], getCellImage(img, {LIGNE: i, COLONNE: j})[VALEUR])

    @unittest.skipIf('getCellImage' not in globals(), 'getCellImage non écrite')
    def test_QUALITE_getCellImage(self):
        pos = {LIGNE: 0, COLONNE: 0}
        self.assertRaises(AssertionError, getCellImage, "blabla", pos)
        img = [[0]*8]*7
        self.assertRaises(AssertionError, getCellImage, img, pos)
        img = [[{VALEUR: 0}] * 10] * 10
        self.assertRaises(AssertionError, getCellImage, img, {LIGNE: 0, COLONNE: "truc"})
        self.assertRaises(AssertionError, getCellImage, img, {LIGNE: "truc", COLONNE: 0})

    @unittest.skipIf('setCellImage' not in globals(), "setCellImage non écrite")
    def test_setCellImage(self):
        for n in range(5, 21):
            img = creerImage(n)
            for i in range(n):
                for j in range(n):
                    pos = {LIGNE: i, COLONNE: j}
                    v = randint(0, 4)
                    setCellImage(img, pos, v)
                    self.assertEqual(v, img[i][j][VALEUR])
                    try:
                        setCellImage(img, pos, None)
                    except AssertionError:
                        self.fail("setCellImage doit accepter la valeur None")

    @unittest.skipIf('setCellImage' not in globals(), 'setCellImage non écrite')
    def test_QUALITE_setCellImage(self):
        pos = {LIGNE: 0, COLONNE: 0}
        self.assertRaises(AssertionError, setCellImage, "blabla", pos, 5)
        img = [[0]*8]*7
        self.assertRaises(AssertionError, setCellImage, img, pos, 5)
        img = [[{VALEUR: 0}] * 10] * 10
        self.assertRaises(AssertionError, setCellImage, img, {LIGNE: 0, COLONNE: "truc"}, 5)
        self.assertRaises(AssertionError, setCellImage, img, {LIGNE: "truc", COLONNE: 0}, 5)
        self.assertRaises(AssertionError, setCellImage, img, pos, "truc")


