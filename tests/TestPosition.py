import unittest

from Model.Position import *
from random import randint


class TestPosition(unittest.TestCase):
    @unittest.skipIf('construirePosition' not in globals(), "Constructeur non écrit")
    def test_construirePosition(self):
        pos = construirePosition()
        self.assertTrue(type_position(pos), "Le constructeur ne renvoie pas une position")
        self.assertEqual(0, pos[LIGNE], "Le constructeur devrait initialiser la ligne à 0")
        self.assertEqual(0, pos[COLONNE], "Le constructeur devrait initialiser la colonne à 0")

    @unittest.skipIf('getLignePosition' not in globals(), "Fonction getLignePosition non écrite")
    def test_getLignePosition(self):
        # test itératif
        pos = {LIGNE: 0, COLONNE: 0}
        for _ in range(50):
            li = randint(0, 10)
            pos[LIGNE] = li
            self.assertEqual(li, getLignePosition(pos), "getLignePosition ne renvoie pas la valeur de la ligne ?")


    @unittest.skipIf('getLignePosition' not in globals(), "Fonction getLignePosition non écrite")
    def test_QUALITE_getLignePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, getLignePosition, "blablabla")
        self.assertRaises(AssertionError, getLignePosition, { LIGNE: 5, "truc": 3})
        self.assertRaises(AssertionError, getLignePosition, { LIGNE: 5, COLONNE: None})
        self.assertRaises(AssertionError, getLignePosition, { "truc": 5, COLONNE: 32})

    @unittest.skipIf('getColonnePosition' not in globals(), "Fonction getColonnePosition non écrite")
    def test_getColonnePosition(self):
        # test itératif
        pos = {LIGNE: 0, COLONNE: 0}
        for _ in range(50):
            li = randint(0, 10)
            pos[COLONNE] = li
            self.assertEqual(li, getColonnePosition(pos), "getColonnePosition ne renvoie pas la valeur de la colonne ?")

    @unittest.skipIf('getColonnePosition' not in globals(), "Fonction getColonnePosition non écrite")
    def test_QUALITE_getColonnePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, getColonnePosition, "blablabla")
        self.assertRaises(AssertionError, getColonnePosition, { LIGNE: 5, "truc": 3})
        self.assertRaises(AssertionError, getColonnePosition, { LIGNE: 5, COLONNE: None})
        self.assertRaises(AssertionError, getColonnePosition, { "truc": 5, COLONNE: 32})

    @unittest.skipIf('setLignePosition' not in globals(), "Fonction setLignePosition non écrite")
    def test_setLignePosition(self):
        # test itératif
        pos = {LIGNE: 0, COLONNE: 0}
        for _ in range(50):
            li = randint(0, 10)
            setLignePosition(pos, li)
            self.assertEqual(li, pos[LIGNE], "setLignePosition ne modifie pas la valeur de la ligne ?")


    @unittest.skipIf('setLignePosition' not in globals(), "Fonction setLignePosition non écrite")
    def test_QUALITE_setLignePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, setLignePosition, "blablabla", 10)
        self.assertRaises(AssertionError, setLignePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, setLignePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, setLignePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, setLignePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, setLignePosition, { LIGNE: 5, COLONNE: 32}, "truc")

    @unittest.skipIf('setColonnePosition' not in globals(), "Fonction setColonnePosition non écrite")
    def test_setColonnePosition(self):
        # test itératif
        pos = {LIGNE: 0, COLONNE: 0}
        for _ in range(50):
            li = randint(0, 10)
            setColonnePosition(pos, li)
            self.assertEqual(li, pos[COLONNE], "setColonnePosition ne modifie pas la valeur de la colonne ?")

    @unittest.skipIf('setColonnePosition' not in globals(), "Fonction setColonnePosition non écrite")
    def test_QUALITE_setColonnePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, setColonnePosition, "blablabla", 10)
        self.assertRaises(AssertionError, setColonnePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, setColonnePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, setColonnePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, setColonnePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, setColonnePosition, { LIGNE: 5, COLONNE: 32}, "truc")

    @unittest.skipIf('incLignePosition' not in globals(), "Fonction incLignePosition non écrite")
    def test_incLignePosition(self):
        pos = {LIGNE: 0, COLONNE: 0}
        # Test de la valeur par défaut
        incLignePosition(pos)
        self.assertEqual(1, pos[LIGNE], "L'appel par défaut (un seul paramètre) à incLignePosition devrait augmenter la ligne de 1")
        li = 1
        for _ in range(10):
            inc = randint(-10, 10)
            incLignePosition(pos, inc)
            li += inc
            self.assertEqual(li, pos[LIGNE], "incLignePosition ne modifie pas correctement la valeur quand l'incrément est renseigné")

    @unittest.skipIf('incLignePosition' not in globals(), "Fonction incLignePosition non écrite")
    def test_QUALITE_incLignePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, incLignePosition, "blablabla")
        self.assertRaises(AssertionError, incLignePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, incLignePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, incLignePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, incLignePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, incLignePosition, { LIGNE: 5, COLONNE: 32}, "truc")

    @unittest.skipIf('incColonnePosition' not in globals(), "Fonction incColonnePosition non écrite")
    def test_incColonnePosition(self):
        pos = {LIGNE: 0, COLONNE: 0}
        # Test de la valeur par défaut
        incColonnePosition(pos)
        self.assertEqual(1, pos[COLONNE], "L'appel par défaut (un seul paramètre) à incColonnePosition devrait augmenter la colonne de 1")
        li = 1
        for _ in range(10):
            inc = randint(-10, 10)
            incColonnePosition(pos, inc)
            li += inc
            self.assertEqual(li, pos[COLONNE], "incColonnePosition ne modifie pas correctement la valeur quand l'incrément est renseigné")

    @unittest.skipIf('incColonnePosition' not in globals(), "Fonction incColonnePosition non écrite")
    def test_QUALITE_incColonnePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, incColonnePosition, "blablabla")
        self.assertRaises(AssertionError, incColonnePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, incColonnePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, incColonnePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, incColonnePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, incColonnePosition, { LIGNE: 5, COLONNE: 32}, "truc")

    @unittest.skipIf('decLignePosition' not in globals(), "Fonction decLignePosition non écrite")
    def test_decLignePosition(self):
        pos = {LIGNE: 0, COLONNE: 0}
        # Test de la valeur par défaut
        decLignePosition(pos)
        self.assertEqual(-1, pos[LIGNE], "L'appel par défaut (un seul paramètre) à decLignePosition devrait décrémenter la ligne de 1")
        li = -1
        for _ in range(10):
            inc = randint(-10, 10)
            decLignePosition(pos, inc)
            li -= inc
            self.assertEqual(li, pos[LIGNE], "decLignePosition ne modifie pas correctement la valeur quand le décrément est renseigné")

    @unittest.skipIf('decLignePosition' not in globals(), "Fonction decLignePosition non écrite")
    def test_QUALITE_decLignePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, decLignePosition, "blablabla")
        self.assertRaises(AssertionError, decLignePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, decLignePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, decLignePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, decLignePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, decLignePosition, { LIGNE: 5, COLONNE: 32}, "truc")

    @unittest.skipIf('decColonnePosition' not in globals(), "Fonction decColonnePosition non écrite")
    def test_decColonnePosition(self):
        pos = {LIGNE: 0, COLONNE: 0}
        # Test de la valeur par défaut
        decColonnePosition(pos)
        self.assertEqual(-1, pos[COLONNE], "L'appel par défaut (un seul paramètre) à decColonnePosition devrait décrémenter la colonne de 1")
        li = -1
        for _ in range(10):
            inc = randint(-10, 10)
            decColonnePosition(pos, inc)
            li -= inc
            self.assertEqual(li, pos[COLONNE], "decColonnePosition ne modifie pas correctement la valeur quand le décrément est renseigné")

    @unittest.skipIf('decColonnePosition' not in globals(), "Fonction decColonnePosition non écrite")
    def test_QUALITE_decColonnePosition_raise_AssertionError(self):
        self.assertRaises(AssertionError, decColonnePosition, "blablabla")
        self.assertRaises(AssertionError, decColonnePosition, { LIGNE: 5, "truc": 3}, 10)
        self.assertRaises(AssertionError, decColonnePosition, { LIGNE: 5, COLONNE: None}, 10)
        self.assertRaises(AssertionError, decColonnePosition, { "truc": 5, COLONNE: 32}, 10)
        self.assertRaises(AssertionError, decColonnePosition, { LIGNE: 5, COLONNE: 32}, None)
        self.assertRaises(AssertionError, decColonnePosition, { LIGNE: 5, COLONNE: 32}, "truc")

