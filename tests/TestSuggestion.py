import unittest

from Model.Suggestion import *



class TestSuggestion(unittest.TestCase):
    @unittest.skipIf('construireSuggestion' not in globals(), "construireSuggestion non écrit")
    def test_construireSuggestion(self):
        pos = {LIGNE: 5, COLONNE: 8}
        sugg = construireSuggestion(pos, 5)
        self.assertTrue(type_suggestion(sugg), "construireSuggestion ne retourne pas le bon dictionnaire")
        self.assertEqual(sugg[POSITION], pos, "construireSuggestion ne prend pas ne compte la position donnée")
        self.assertEqual(sugg[COULEUR], 5, "construireSuggestion ne prend pas en compte la couleur donnée")

    @unittest.skipIf('getPositionSuggestion' not in globals(), "getPositionSuggestion non écrit")
    def test_getPositionSuggestion(self):
        pos = {LIGNE: 5, COLONNE: 8}
        sugg = {POSITION: pos, COULEUR: 5}
        self.assertEqual(pos, getPositionSuggestion(sugg))

    @unittest.skipIf('getPositionSuggestion' not in globals(), "getPositionSuggestion non écrit")
    def test_QUALITE_getPositionSuggestion(self):
        pos = {LIGNE: 5, COLONNE: 8}
        sugg = {POSITION: {LIGNE: "5", COLONNE: 6}, COULEUR: 5}
        self.assertRaises(AssertionError, getPositionSuggestion, sugg)
        sugg = {POSITION: {LIGNE: 5, COLONNE: "6"}, COULEUR: 5}
        self.assertRaises(AssertionError, getPositionSuggestion, sugg)
        sugg = {POSITION: {LIGNE: 5, COLONNE: 6}, COULEUR: "5"}
        self.assertRaises(AssertionError, getPositionSuggestion, sugg)
        self.assertRaises(AssertionError, getPositionSuggestion, "...")

    @unittest.skipIf('getCouleurSuggestion' not in globals(), "getCouleurSuggestion non écrit")
    def test_getCouleurSuggestion(self):
        pos = {LIGNE: 5, COLONNE: 8}
        sugg = {POSITION: pos, COULEUR: 5}
        self.assertEqual(5, getCouleurSuggestion(sugg))

    @unittest.skipIf('getCouleurSuggestion' not in globals(), "getCouleurSuggestion non écrit")
    def test_QUALITE_getCouleurSuggestion(self):
        pos = {LIGNE: 5, COLONNE: 8}
        sugg = {POSITION: {LIGNE: "5", COLONNE: 6}, COULEUR: 5}
        self.assertRaises(AssertionError, getCouleurSuggestion, sugg)
        sugg = {POSITION: {LIGNE: 5, COLONNE: "6"}, COULEUR: 5}
        self.assertRaises(AssertionError, getCouleurSuggestion, sugg)
        sugg = {POSITION: {LIGNE: 5, COLONNE: 6}, COULEUR: "5"}
        self.assertRaises(AssertionError, getCouleurSuggestion, sugg)
        self.assertRaises(AssertionError, getCouleurSuggestion, "...")


