#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/10 17:43:42.301951
# ------------------------------------------------------------------------------
import requests as r
import json
import unittest

from src.coingecko_api.coingecko_api import CoinGecko
# ------------------------------------------------------------------------------
class TestCoinGecko_API(unittest.TestCase):

    @staticmethod
    def get(url):
        return json.loads(r.get(url).text)

    # Getters ------------------------------------------------------------------
    def test_get_url_base(self):
        url_base = 'https://api.coingecko.com/api/v3/'
        cg = CoinGecko()

        self.assertEqual(cg.get_url_base(), url_base)

    # --------------------------------------------------------------------------

    def test_ping(self):
        url = 'https://api.coingecko.com/api/v3/ping'
        cg = CoinGecko()

        self.assertEqual(cg.ping(), self.get(url))

# ------------------------------------------------------------------------------

