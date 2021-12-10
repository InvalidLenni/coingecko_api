#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/10 16:44:23.128361
#+ Editado:	2021/12/10 16:47:25.348229
# ------------------------------------------------------------------------------
import unittest

from src.coingecko_api.cg_uteis import check_types, e_bisesto, unix2human
# ------------------------------------------------------------------------------
class TestCG_Uteis(unittest.TestCase):

    def test_check_types(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    # para que corran os testes
    unittest.main()
# ------------------------------------------------------------------------------

