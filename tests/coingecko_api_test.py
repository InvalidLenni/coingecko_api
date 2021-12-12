#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/12 16:29:15.583244
# ------------------------------------------------------------------------------
import requests as r
import json
import unittest

from src.coingecko_api.coingecko_api import CoinGecko
from src.coingecko_api.excepcions import ErroTipado
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

    def test_get_price_erro(self):
        """
        Testeo de ter metido un tipo de entrada que non entra dentro do especificado
        """
        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_price(['bitcoin'], [0])

    def test_get_price(self):
        """
        Probas básicas do uso normal.
        """
        probas_ids = ['bitcoin', ['bitcoin', 'ethereum']]
        probas_vs_currencies = ['eur', ['eur', 'usd']]
        cg = CoinGecko()

        for iden, vs_curren in zip(probas_ids, probas_vs_currencies):
            if type(iden) == list:
                iden2 = ','.join(iden)
            else:
                iden2 = iden

            if type(vs_curren) == list:
                vs_curren2 = ','.join(vs_curren)
            else:
                vs_curren2 = vs_curren

            url = f'https://api.coingecko.com/api/v3/simple/price?ids={iden2}&vs_currencies={vs_curren2}&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
            self.assertEqual(cg.get_price(iden, vs_curren), self.get(url))

            url = f'https://api.coingecko.com/api/v3/simple/price?ids={iden2}&vs_currencies={vs_curren2}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true'
            self.assertEqual(cg.get_price(iden, vs_curren, True, True, True, True), self.get(url))

    def test_get_token_price(self):
        """
        Probas básicas dun uso normal.
        """
        pass

# ------------------------------------------------------------------------------

