import unittest

from Model.Cellule import *



class TestCellule(unittest.TestCase):
    @unittest.skipIf('construireCellule' not in globals(), "construireCellule non écrit")
    def test_construireCellule(self):
        cell = construireCellule()
        self.assertTrue(type_cellule(cell), "L'objet retourné ne correspond pas à un dictionnaire avec unique clé VALEUR")
        self.assertIsNone(cell[VALEUR], "La 'valeur' de la cellule devrait être None")

    @unittest.skipIf('isVuCellule' not in globals(),
                     "isVuCellule non écrit")
    def test_isVuCellule(self):
        cell = dict()
        cell[VALEUR] = None
        self.assertFalse(isVuCellule(cell), "La cellule contenant None devrait ne pas être connue")
        for i in range(10):
            cell[VALEUR] = i
            self.assertTrue(isVuCellule(cell), "La cellule ne contenant pas None devrait être connue")

    @unittest.skipIf('isVuCellule' not in globals(), "Fonction isVuCellule non écrite")
    def test_QUALITE_isVuCellule_raise_AssertionError(self):
        self.assertRaises(AssertionError, isVuCellule, dict())
        self.assertRaises(AssertionError, isVuCellule, {"V" : 5})
        self.assertRaises(AssertionError, isVuCellule, 40)
        self.assertRaises(AssertionError, isVuCellule, "Cellule")

    @unittest.skipIf('isVideCellule' not in globals(),
                     "isVideCellule non écrit")
    def test_isVideCellule(self):
        cell = dict()
        cell[VALEUR] = None
        self.assertFalse(isVideCellule(cell), "La cellule contenant None devrait ne pas être vide")
        cell[VALEUR] = 0
        self.assertTrue(isVideCellule(cell), "La cellule contenant 0 devrait être vide")
        for i in range(1, 10):
            cell[VALEUR] = i
            self.assertFalse(isVideCellule(cell), "La cellule ne contenant pas 0 ne devrait être vide")

    @unittest.skipIf('isVideCellule' not in globals(), "Fonction isVideCellule non écrite")
    def test_QUALITE_isVideCellule_raise_AssertionError(self):
        self.assertRaises(AssertionError, isVideCellule, dict())
        self.assertRaises(AssertionError, isVideCellule, {"V" : 5})
        self.assertRaises(AssertionError, isVideCellule, 40)
        self.assertRaises(AssertionError, isVideCellule, "Cellule")

    @unittest.skipIf('getCouleurCellule' not in globals(), "Fonction getCouleurCellule non écrite")
    def test_getCouleurCellule(self):
        cell = dict()
        for i in range(10):
            cell[VALEUR] = i
            self.assertEqual(i, getCouleurCellule(cell), f"La cellule devrait contenir {i} comme couleur, 0 étant considéré ici comme une couleur.")

    @unittest.skipIf('getCouleurCellule' not in globals(), "Fonction getCouleurCellule non écrite")
    def test_QUALITE_getCouleurCellule(self):
        self.assertRaises(AssertionError, getCouleurCellule, dict())
        self.assertRaises(AssertionError, getCouleurCellule, {"V" : 5})
        self.assertRaises(AssertionError, getCouleurCellule, 40)
        self.assertRaises(AssertionError, getCouleurCellule, "Cellule")

    @unittest.skipIf('setCouleurCellule' not in globals(), "Fonction setCouleurCellule non écrite")
    def test_setCouleurCellule(self):
        cell = {VALEUR: None}
        for i in range(10):
            setCouleurCellule(cell, i)
            self.assertEqual(i, cell[VALEUR], "La fonction ne modifie pas correctement la couleur de la cellule, 0 étant considéré ici comme une couleur.")

    @unittest.skipIf('setCouleurCellule' not in globals(), "Fonction setCouleurCellule non écrite")
    def test_QUALITE_setCouleurCellule_raise_AssertionError(self):
        self.assertRaises(AssertionError, setCouleurCellule, dict(), 0)
        self.assertRaises(AssertionError, setCouleurCellule, {"V" : 5}, 0)
        self.assertRaises(AssertionError, setCouleurCellule, 40, 0)
        self.assertRaises(AssertionError, setCouleurCellule, "Cellule", 0)
        cell = {VALEUR: None}
        self.assertRaises(AssertionError, setCouleurCellule, cell, None)
        self.assertRaises(AssertionError, setCouleurCellule, cell, "valeur")
        self.assertRaises(AssertionError, setCouleurCellule, cell, dict())

    @unittest.skipIf('setNonVuCellule' not in globals(), "Fonction setNonVuCellule non écrite")
    def test_setNonVuCellule(self):
        cell = {VALEUR: 10}
        setNonVuCellule(cell)
        self.assertIsNone(cell[VALEUR], "La fonction ne modifie pas correctement la valeur de la cellule qui devrait être à None.")

    @unittest.skipIf('setNonVuCellule' not in globals(), "Fonction setNonVuCellule non écrite")
    def test_QUALITE_setNonVuCellule_raise_AssertionError(self):
        self.assertRaises(AssertionError, setNonVuCellule, dict())
        self.assertRaises(AssertionError, setNonVuCellule, {"V" : 5})
        self.assertRaises(AssertionError, setNonVuCellule, 40)
        self.assertRaises(AssertionError, setNonVuCellule, "Cellule")
