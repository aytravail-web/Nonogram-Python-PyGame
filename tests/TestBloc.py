import unittest

from random import randint
from Model.Bloc import *



class TestBloc(unittest.TestCase):
    @unittest.skipIf('construireBloc' not in globals(), "construireBloc non écrit")
    def test_construireBloc(self):
        bloc = construireBloc(5, 10)
        self.assertTrue(type_bloc(bloc), "L'objet retourné ne correspond pas à un bloc")
        self.assertEqual(5, bloc[NOMBRE], "Le premier paramètre doit correspondre à la clé NOMBRE")
        self.assertEqual(10, bloc[COULEUR], "Le second paramètre doit correspondre à la clé COULEUR")
        self.assertFalse(bloc[VU], "La valeur associée à la clé VU doit valoir False")

    @unittest.skipIf('construireBloc' not in globals(), "construireBloc non écrit")
    def test_QUALITE_construireBloc(self):
        self.assertRaises(AssertionError, construireBloc, "string", 10)
        self.assertRaises(AssertionError, construireBloc, 5, "string")
        for i in range(-5,1):
            self.assertRaises(AssertionError, construireBloc, i, 5)
            self.assertRaises(AssertionError, construireBloc, 5, i)

    @unittest.skipIf('getNombreBloc' not in globals() or 'getCouleurBloc' not in globals() or 'isVuBloc' not in globals(),
                     "getNombreBloc ou getCouleurBloc ou isVuBloc non écrit")
    def test_get_Nombre_Couleur_Vu_Bloc(self):
        for _ in range(10):
            nb = randint(1,15)
            col = randint(1,4)
            vu = randint(1,2) == 1
            bloc = {NOMBRE: nb, COULEUR: col, VU: vu}
            self.assertEqual(nb, getNombreBloc(bloc), "Revoir le getter sur Nombre")
            self.assertEqual(col, getCouleurBloc(bloc), "Revoir le getter sur Couleur")
            self.assertEqual(vu, isVuBloc(bloc), "Revoir le getter sur Vu")

    @unittest.skipIf('getNombreBloc' not in globals(), "getNombreBloc non écrit")
    def test_QUALITE_getNombreBloc(self):
        self.assertRaises(AssertionError, getNombreBloc, "string")
        self.assertRaises(AssertionError, getNombreBloc, 10)
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:5, COULEUR: 3})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:5, VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {COULEUR:5, VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:0, COULEUR:1, VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:"1", COULEUR:1, VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:1, COULEUR:"1", VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:1, COULEUR:0, VU: False})
        self.assertRaises(AssertionError, getNombreBloc, {NOMBRE:1, COULEUR:1, VU: 3})

    @unittest.skipIf('getCouleurBloc' not in globals(), "getCouleurBloc non écrit")
    def test_QUALITE_getCouleurBloc(self):
        self.assertRaises(AssertionError, getCouleurBloc, "string")
        self.assertRaises(AssertionError, getCouleurBloc, 10)
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:5, COULEUR: 3})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:5, VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {COULEUR:5, VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:0, COULEUR:1, VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:"1", COULEUR:1, VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:1, COULEUR:"1", VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:1, COULEUR:0, VU: False})
        self.assertRaises(AssertionError, getCouleurBloc, {NOMBRE:1, COULEUR:1, VU: 3})

    @unittest.skipIf('isVuBloc' not in globals(), "isVuBloc non écrit")
    def test_QUALITE_isVuBloc(self):
        self.assertRaises(AssertionError, isVuBloc, "string")
        self.assertRaises(AssertionError, isVuBloc, 10)
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:5, COULEUR: 3})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:5, VU: False})
        self.assertRaises(AssertionError, isVuBloc, {COULEUR:5, VU: False})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:0, COULEUR:1, VU: False})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:"1", COULEUR:1, VU: False})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:1, COULEUR:"1", VU: False})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:1, COULEUR:0, VU: False})
        self.assertRaises(AssertionError, isVuBloc, {NOMBRE:1, COULEUR:1, VU: 3})

    @unittest.skipIf('setVuBloc' not in globals(), "setVuBloc non écrit")
    def test_setVuBloc(self):
        bloc = {NOMBRE: 1, COULEUR: 1, VU: False}
        for _ in range(10):
            vu = randint(0, 1) == 0
            setVuBloc(bloc, vu)
            self.assertEqual(vu, bloc[VU], "Revoir le setter sur VU")

    @unittest.skipIf('setVuBloc' not in globals(), "setVuBloc non écrit")
    def test_QUALITE_setVuBloc(self):
        self.assertRaises(AssertionError, setVuBloc, "string", False)
        self.assertRaises(AssertionError, setVuBloc, 10, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:5, COULEUR: 3}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:5, VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {COULEUR:5, VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:0, COULEUR:1, VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:"1", COULEUR:1, VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:1, COULEUR:"1", VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:1, COULEUR:0, VU: False}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:1, COULEUR:1, VU: 3}, False)
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:1, COULEUR:1, VU: True}, "False")
        self.assertRaises(AssertionError, setVuBloc, {NOMBRE:1, COULEUR:1, VU: True}, 1)

