#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/10 16:44:23.128361
#+ Editado:	2021/12/10 18:05:48.314569
# ------------------------------------------------------------------------------
import unittest

from src.coingecko_api.cg_uteis import check_types, e_bisesto, unix2human
from src.coingecko_api.excepcions import ErroTipado
# ------------------------------------------------------------------------------
class TestCG_Uteis(unittest.TestCase):

    # check_types --------------------------------------------------------------
    def test_check_types_1(self):
        """
        Entradas simples como lista

        True
        """

        self.assertTrue(check_types(['a'], [str]))
        self.assertTrue(check_types([0], [int]))
        self.assertTrue(check_types([True], [bool]))

    def test_check_types_2(self):
        """
        Entradas simples sen listas
        """

        self.assertTrue(check_types('e', str))
        self.assertTrue(check_types(1, int))
        self.assertTrue(check_types(False, bool))

    # entradas simples como lista variada
    def test_check_types_3(self):
        self.assertTrue(check_types(['', 0, True], [str, int, bool]))

    # entradas simples como variable sola: int
    def test_check_types_4(self):
        self.assertTrue(check_types(0, int))

    # entradas simples como variable sola: bool
    def test_check_types_5(self):
        self.assertTrue(check_types(False, bool))

    # entradas simples como lista: int
    def test_check_types_6(self):
        self.assertTrue(check_types([0], [int]))

    # entradas simples como lista: bool
    def test_check_types_7(self):
        self.assertTrue(check_types([False], [bool]))

    # entradas simples como lista: bool as int
    def test_check_types_8(self):
        self.assertFalse(check_types([False], [int]))

    # entradas simples como lista: int as bool
    def test_check_types_9(self):
        self.assertFalse(check_types(0, bool))

    # entradas simples como lista: str as int
    def test_check_types_10(self):
        self.assertFalse(check_types('', int))

    # listas con un elemento mal posto
    def test_check_types_11(self):
        self.assertFalse(check_types(['', 0, 0, True], [str, int, str, bool]))

    # erro de listas con diferentes lonxitudes
    def test_check_types_12(self):
        with self.assertRaises(ErroTipado):
            check_types([1,2], int)

    # listas con lista acertando
    def test_check_types_13(self):
        self.assertTrue(check_types(['', 0, [0, 'a'], True], [str, int, [int, str], bool]))

    # listas con lista errando
    def test_check_types_14(self):
        self.assertFalse(check_types(['', 0, [0, 'a'], True], [str, int, list, bool]))

# ------------------------------------------------------------------------------

