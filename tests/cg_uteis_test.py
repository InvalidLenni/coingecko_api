#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/10 16:44:23.128361
#+ Editado:	2021/12/10 20:44:53.469575
# ------------------------------------------------------------------------------
import unittest

from src.coingecko_api.cg_uteis import check_types, e_bisesto, unix2human
from src.coingecko_api.excepcions import ErroTipado
# ------------------------------------------------------------------------------
class TestCG_Uteis(unittest.TestCase):

    # check_types --------------------------------------------------------------
    def test_check_types_simples_non_lista(self):
        """
        Entradas simples sen listas.
        """

        # true
        self.assertTrue(check_types('e', str))
        self.assertTrue(check_types(1, int))
        self.assertTrue(check_types(False, bool))
        self.assertTrue(check_types([[[]]], list))

        #false
        self.assertFalse(check_types([[]], list))       # [[]]   ? list
        self.assertFalse(check_types(0, bool))
        self.assertFalse(check_types('', int))

        # ErroTipado
        with self.assertRaises(ErroTipado):
            check_types([], list)

    def test_check_types_simples_lista(self):
        """
        Entradas simples como lista.
        """

        # true
        self.assertTrue(check_types(['a'], [str]))      # [str]  ? [str]
        self.assertTrue(check_types([0], [int]))        # [int]  ? [int]
        self.assertTrue(check_types([True], [bool]))    # [bool] ? [bool]
        self.assertTrue(check_types([[[]]], [list]))    # [[[]]] ? [list]
        #

        # false
        self.assertFalse(check_types([[]], [list]))     # [[]]   ? [list]

        self.assertFalse(check_types(['b'], [int]))     # [str]  ? [int]
        self.assertFalse(check_types(['c'], [bool]))    # [str]  ? [bool]
        self.assertFalse(check_types(['d'], [list]))    # [str]  ? [list]

        self.assertFalse(check_types([False], [int]))   # [bool] ? [int]
        self.assertFalse(check_types([True], [str]))    # [bool] ? [str]
        self.assertFalse(check_types([True], [list]))   # [bool] ? [list]
        #

    def test_check_types_3(self):
        """
        Entradas complexas
        """

        # true
        self.assertTrue(check_types(['', 0, True], [str, int, bool]))

    """
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
    """

# ------------------------------------------------------------------------------

