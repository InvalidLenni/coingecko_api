#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/09 22:21:58.806502
# ------------------------------------------------------------------------------
import unittest

from src.coingecko_api.coingecko_api import CoinGecko
# ------------------------------------------------------------------------------
class TestCoinGecko_API(unittest.TestCase):

    def test_ping(self):
        cg = CoinGecko()
        self.assertEqual(cg.ping(),cg.ping())

if __name__ == '__main__':
    # para que corran os testes
    unittest.main()
# ------------------------------------------------------------------------------

