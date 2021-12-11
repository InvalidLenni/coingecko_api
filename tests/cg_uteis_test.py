#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/10 16:44:23.128361
#+ Editado:	2021/12/11 21:02:47.619198
# ------------------------------------------------------------------------------
import unittest

from src.coingecko_api.cg_uteis import check_types, e_bisesto, unix2human
from src.coingecko_api.excepcions import ErroTipado
# ------------------------------------------------------------------------------
class TestCG_Uteis(unittest.TestCase):

    # check_types --------------------------------------------------------------
    def test_check_types_simples(self):
        """
        Entradas simples sen lista.
        """

        # true
        self.assertTrue(check_types('e', str))          # str   ? str
        self.assertTrue(check_types(1, int))            # int   ? int
        self.assertTrue(check_types(False, bool))       # bool  ? bool
        self.assertTrue(check_types([], list))          # []    ? list
        self.assertTrue(check_types([[]], list))        # [[]]  ? list
        #

        #false
        self.assertFalse(check_types('', int))          # str   ? int
        self.assertFalse(check_types('', bool))         # str   ? bool
        self.assertFalse(check_types('', list))         # str   ? list

        self.assertFalse(check_types(0, str))           # int   ? str
        self.assertFalse(check_types(0, bool))          # int   ? bool
        self.assertFalse(check_types(0, list))          # int   ? list

        self.assertFalse(check_types(True, int))        # bool  ? int
        self.assertFalse(check_types(False, str))       # bool  ? str
        self.assertFalse(check_types(False, list))      # bool  ? list
        #

        # ErroTipado
        with self.assertRaises(ErroTipado):
            check_types([], int)
            check_types([], bool)
            check_types([], str)

            check_types([[]], str)
            check_types([[]], int)
            check_types([[]], bool)

            check_types([[[]]], str)
            check_types([[[]]], int)
            check_types([[[]]], bool)

            # etc
        #

    def test_check_types_simples_lista(self):
        """
        Entradas simples como lista.
        """

        # true
        self.assertTrue(check_types(['a'], [str]))      # [str]  ? [str]
        self.assertTrue(check_types([0], [int]))        # [int]  ? [int]
        self.assertTrue(check_types([True], [bool]))    # [bool] ? [bool]
        self.assertTrue(check_types([[]], [list]))      # [[]]   ? [list]
        self.assertTrue(check_types([[[]]], [list]))    # [[[]]] ? [list]
        #

        # false
        self.assertFalse(check_types(['b'], [int]))     # [str]  ? [int]
        self.assertFalse(check_types(['c'], [bool]))    # [str]  ? [bool]
        self.assertFalse(check_types(['d'], [list]))    # [str]  ? [list]

        self.assertFalse(check_types([1], [str]))       # [int]  ? [str]
        self.assertFalse(check_types([2], [bool]))      # [int]  ? [bool]
        self.assertFalse(check_types([3], [list]))      # [int]  ? [list]

        self.assertFalse(check_types([False], [int]))   # [bool] ? [int]
        self.assertFalse(check_types([True], [str]))    # [bool] ? [str]
        self.assertFalse(check_types([True], [list]))   # [bool] ? [list]
        #

        # ErroTipado
        with self.assertRaises(ErroTipado):
            check_types([], [int])
            check_types([], [bool])
            check_types([], [bool])

            check_types([[]], [str])
            check_types([[]], [int])
            check_types([[]], [bool])

            check_types([[[]]], [str])
            check_types([[[]]], [int])
            check_types([[[]]], [bool])

            # etc
        #

    def test_check_types_complexas(self):
        """
        Entradas complexas.
        """

        # true
        self.assertTrue(check_types(['', 0, True], [str, int, bool]))
        self.assertTrue(check_types([0, 9, True], [int, int, bool]))

        self.assertTrue(check_types(['', 0, [0], True], [str, int, [int], bool]))
        self.assertTrue(check_types(['', 0, [0], True], [str, int, [int], bool]))
        self.assertTrue(check_types(['', 0, [0], True], [str, int, int, bool]))
        self.assertTrue(check_types(['', 0, [0, 'a'], True], [str, int, [int, str], bool]))
        self.assertTrue(check_types(['', 0, [0, 100], True], [str, int, [int, int], bool]))

        self.assertTrue(check_types(['', 0, [0, [100, 'a']], True], [str, int, [int, [int, str]], bool]))
        self.assertTrue(check_types(['', 0, [0, [100, 'a', [False]]], True], [str, int, [int, [int, str, [bool]]], bool]))
        self.assertTrue(check_types(['', 0, [0, [100, 'a', [False]]], True], [str, int, [int, [int, str, bool]], bool]))
        #

        # false
        self.assertFalse(check_types(['', 0, 0, True], [str, int, str, bool]))
        self.assertFalse(check_types(['', 0, False, True], [str, int, str, bool]))

        self.assertFalse(check_types(['', 0, [0], True], [str, int, str, bool]))
        self.assertFalse(check_types(['', 0, [0], True], [str, int, [str], bool]))
        self.assertFalse(check_types(['', 0, [0], True], [str, int, [int], int]))
        self.assertFalse(check_types(['', 0, [0], True], [str, int, int, int]))
        #

        # ErroTipado
        with self.assertRaises(ErroTipado):
            check_types(['', 0, [0, 'a'], True], [str, int, list, bool])
            check_types(['', 0, [0, [100, 'a', [False]]], True], [str, int, [int, int, str, bool], bool])
        #

    def test_check_types_listas_distintas_lonxitudes(self):
        """
        Cando se meten dúas lista de distintas lonxitudes.
        """

        # ErroTipado
        with self.assertRaises(ErroTipado):
            check_types([1,2], int)
            check_types([1,2], [int, int, bool])
        #

    # e_bisesto ----------------------------------------------------------------
    def test_e_bisesto(self):
        anos_bisestos = [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

        for ano in range(1584, 2022):
            if ano in anos_bisestos:
                self.assertTrue(e_bisesto(ano))
            else:
                self.assertFalse(e_bisesto(ano))

    # unix2human ---------------------------------------------------------------
    def test_unix2human(self):
        """
        Dada unha data en unix devolve unha gregoriana
        """

        # true
        self.assertTrue(unix2human(1638130186), '2021/11/28 21:09:46')
        self.assertTrue(unix2human(1638130186000), '2021/11/28 21:09:46')           # fai un tope no décimo número
        self.assertTrue(unix2human(1638130186, '-'), '2021-11-28 21:09:46')
        self.assertTrue(unix2human(1638130186, '-', '_'), '2021-11-28 21_09_46')

# ------------------------------------------------------------------------------

