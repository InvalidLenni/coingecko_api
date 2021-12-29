#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/29 13:02:32.197004
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

    # PING ---------------------------------------------------------------------

    # /ping
    def test_ping(self):
        url = 'https://api.coingecko.com/api/v3/ping'
        cg = CoinGecko()

        self.assertEqual(cg.ping(), self.get(url))

    # PING # -------------------------------------------------------------------

    # SIMPLE -------------------------------------------------------------------

    # /simple/price
    def test_get_price_erro(self):
        """
        Testeo de ter metido un tipo de entrada que non entra dentro do especificado.
        """
        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_price(['bitcoin'], [0])

    # /simple/price
    def test_get_price(self):
        """
        Probas básicas do uso normal.
        """
        probas_ids = ['bitcoin', 'bitcoin,ethereum', ['bitcoin', 'ethereum']]
        probas_vs_currencies = ['eur', 'eur,usd', ['eur', 'usd']]
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

    # /simple/token_price/{id}
    def test_get_token_price_erro(self):
        """
        Proba con entradas erróneas.
        """
        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_token_price('ethereum', False, 7)

    # /simple/token_price/{id}
    def test_get_token_price(self):
        """
        Probas básicas dun uso normal.
        """
        gooddollar = '0x67C5870b4A41D4Ebef24d2456547A03F1f3e094B'
        tether = '0xdac17f958d2ee523a2206206994597c13d831ec7'
        whackd = '0xcf8335727b776d190f9d15a54e6b9b9348439eee'

        lista_moedas = ['ethereum', 'ethereum', 'ethereum']
        lista_tokens = [gooddollar, [tether, whackd], whackd]
        lista_divisas = ['usd', 'eur,usd', ['eur', 'usd']]

        cg = CoinGecko()

        for moeda, token, divisa in zip(lista_moedas, lista_tokens, lista_divisas):
            if type(token) == list:
                token2 = ','.join(token)
            else:
                token2 = token

            if type(divisa) == list:
                divisa2 = ','.join(divisa)
            else:
                divisa2 = divisa

            url = f'https://api.coingecko.com/api/v3/simple/token_price/{moeda}?contract_addresses={token2}'\
                    f'&vs_currencies={divisa2}&include_market_cap=false&include_24hr_vol=false&'\
                    f'include_24hr_change=false&include_last_updated_at=false'

            self.assertEqual(cg.get_token_price(moeda, token, divisa), self.get(url))

            url = f'https://api.coingecko.com/api/v3/simple/token_price/{moeda}?contract_addresses={token2}'\
                    f'&vs_currencies={divisa2}&include_market_cap=true&include_24hr_vol=true&'\
                    f'include_24hr_change=true&include_last_updated_at=true'

            self.assertEqual(cg.get_token_price(moeda, token, divisa, True, True, True, True), self.get(url))

    # /simple/supported_vs_currencies
    def test_get_supported_vs_currencies(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = cg.get_url_base()+'simple/supported_vs_currencies'

        self.assertEqual(cg.get_supported_vs_currencies(), self.get(url))

    # SIMPLE # -----------------------------------------------------------------

    # COINS --------------------------------------------------------------------

    # /coins/list
    def test_get_coin_list(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = cg.get_url_base()+'coins/list'

        self.assertEqual(cg.get_coins_list(), self.get(url))

    # /coin/markets
    def test_get_coins_markets_erro(self):
        """
        Entrada incorrecta.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_coins_markets(0, '', '')

    # /coin/markets
    def test_get_coins_markets(self):
        """
        Uso normal.
        """

        moedas_vs =     ['usd', 'eur', 'usd', 'eur', 'usd']
        moedas =        ['bitcoin', 'bitcoin, ethereum', ['bitcoin', 'ethereum'], None, None]
        categorias =    [None, None, None, 'aave-tokens', 'analytics']
        ordes =         ['market_cap_desc', 'market_cap_desc', 'gecko_desc', 'volume_asc', 'id_desc']
        xpaxs =         [250, 100, 200, 50, 5]
        paxs =          [0, 4, 1, 0, 5]
        sparklines =    [False, True, True, False, True]
        pcps =          [['1h', '24h', '7d'], '7d', '1d', '1d', '24h']

        cg = CoinGecko()

        for moeda_vs, moeda, categoria, orde, xpax, pax, sparkline, pcp in\
            zip(moedas_vs, moedas, categorias, ordes, xpaxs, paxs, sparklines, pcps):

            if type(pcp) != list:
                pcp = [pcp]
            if type(moeda) != list:
                moeda = [moeda]

            if categoria:
                url = cg.get_url_base()+f'coins/markets?vs_currency={moeda_vs}'\
                    f'&category={categoria}&order={orde}&per_page={xpax}'\
                    f'&page={pax}&sparkline={str(sparkline).lower()}&price_change_percentage='+','.join(pcp)

                print(url)

                resultado = cg.get_coins_markets(moeda_vs, categoria=categoria, orde=orde,
                                xpax=xpax, pax=pax, sparkline=sparkline, cambio_prezo_porcentaxe=pcp)
            elif moeda:
                url = cg.get_url_base()+f'coins/markets?vs_currency={moeda_vs}'\
                    +'&ids='+','.join(moeda)+f'&order={orde}&per_page={xpax}'\
                    f'&page={pax}&sparkline={str(sparkline).lower()}&price_change_percentage='+','.join(pcp)

                resultado = cg.get_coins_markets(moeda_vs, ids_moedas=moeda, orde=orde,
                                xpax=xpax, pax=pax, sparkline=sparkline, cambio_prezo_porcentaxe=pcp)

            self.assertEqual(resultado, self.get(url))

    # /coins
    def test_get_coins(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        self.assertEqual(cg.get_coins(), self.get(cg.get_url_base()+'coins'))

    # /coins/{id}

    # /coins/{id}/tickers

    # /coins/{id}/history

    # /coins/{id}/market_chart

    # /coins/{id}/market_chart/range

    # /coins/{id}/status_updates

    # /coins/{id}/ohlc


    # COINS # ------------------------------------------------------------------


# ------------------------------------------------------------------------------

