#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/11 21:51:50.660699
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

    def test_get_price(self):
        probas_ids = ['bitcoin', ['bitcoin', 'ethereum']]
        probas_vs_currencies = ['eur', ['eur', 'usd']]
        cg = CoinGecko()

        url = f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur,usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
        self.assertEqual(cg.get_price(['bitcoin', 'ethereum'], ['eur', 'usd']), self.get(url))
        #for identificador, vs_currencies in zip(probas_ids, probas_vs_currencies):
            #url = f'https://api.coingecko.com/api/v3/simple/price?ids={identificador}&vs_currencies={vs_currencies}&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'

            #self.assertEqual(cg.get_price(identificador, vs_currencies), self.get(url))

# ------------------------------------------------------------------------------

