#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/09 22:13:41.735240
#+ Editado:	2021/12/31 20:34:11.868807
# ------------------------------------------------------------------------------
import requests as r
import json
import time
import unittest

from src.coingecko_api.coingecko_api import CoinGecko
from src.coingecko_api.excepcions import ErroTipado, ErroData
# ------------------------------------------------------------------------------
class TestCoinGecko_API(unittest.TestCase):

    @staticmethod
    def get(url):
        return json.loads(r.get(url).text)

    @staticmethod
    def get_url_base():
        return 'https://api.coingecko.com/api/v3/'

    '''
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

            url = self.get_url_base()+f'simple/price?ids={iden2}&vs_currencies={vs_curren2}&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false'
            self.assertEqual(cg.get_price(iden, vs_curren), self.get(url))

            url = self.get_url_base()+f'simple/price?ids={iden2}&vs_currencies={vs_curren2}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true'
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

            url = self.get_url_base()+f'simple/token_price/{moeda}?contract_addresses={token2}'\
                    f'&vs_currencies={divisa2}&include_market_cap=false&include_24hr_vol=false&'\
                    f'include_24hr_change=false&include_last_updated_at=false'

            self.assertEqual(cg.get_token_price(moeda, token, divisa), self.get(url))

            url = self.get_url_base()+f'simple/token_price/{moeda}?contract_addresses={token2}'\
                    f'&vs_currencies={divisa2}&include_market_cap=true&include_24hr_vol=true&'\
                    f'include_24hr_change=true&include_last_updated_at=true'

            self.assertEqual(cg.get_token_price(moeda, token, divisa, True, True, True, True), self.get(url))

    # /simple/supported_vs_currencies
    def test_get_supported_vs_currencies(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'simple/supported_vs_currencies'

        self.assertEqual(cg.get_supported_vs_currencies(), self.get(url))

    # SIMPLE # -----------------------------------------------------------------

    # COINS --------------------------------------------------------------------

    # /coins/list
    def test_get_coin_list(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/list'

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
                url = self.get_url_base()+f'coins/markets?vs_currency={moeda_vs}'\
                    f'&category={categoria}&order={orde}&per_page={xpax}'\
                    f'&page={pax}&sparkline={str(sparkline).lower()}&price_change_percentage='+','.join(pcp)

                print(url)

                resultado = cg.get_coins_markets(moeda_vs, categoria=categoria, orde=orde,
                                xpax=xpax, pax=pax, sparkline=sparkline, cambio_prezo_porcentaxe=pcp)
            elif moeda:
                url = self.get_url_base()+f'coins/markets?vs_currency={moeda_vs}'\
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
    def test_get_coin_erro(self):
        """
        Entrada incorrecta.
        """
        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_coin(0)

    # /coins/{id}
    def test_get_coin(self):
        """
        Uso normal.
        Faltaría probar máis casos.
        """

        cg = CoinGecko()

        self.assertEqual(cg.get_coin('bitcoin'), self.get(cg.get_url_base()+'coins/bitcoin'))

    # /coins/{id}/tickers
    def test_get_coin_tickers_erros(self):
        """
        Entrada incorrecta.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_coin_tickers(0)

    # /coins/{id}/tickers
    def test_get_coin_tickers(self):
        """
        Uso normal.
        Faltan casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/bitcoin/tickers?include_exchange_logo=false&page=0&order=trust_score_asc&depth=false'
        self.assertEqual(cg.get_coin_tickers('bitcoin'), self.get(url))

        url = self.get_url_base()+'coins/bitcoin/tickers?exchange_ids=aax,gdax&include_exchange_logo=true&page=0&order=trust_score_asc&depth=false'
        self.assertEqual(cg.get_coin_tickers(id_moeda='bitcoin', ids_exchanges=['aax', 'gdax'], logo_exchange=True), self.get(url))

    # /coins/{id}/history
    def test_get_coin_history_erro(self):
        """
        Entradas incorrectas
        """

        cg = CoinGecko()

        with self.assertRaises(ErroData):
            # non ten tantos días
            cg.get_coin_history('bitcoin', 2021, 2, 31)

        with self.assertRaises(ErroData):
            # non é ano bisesto
            cg.get_coin_history('bitcoin', 2021, 2, 29)

        with self.assertRaises(ErroData):
            # ten máximo 30 días
            cg.get_coin_history('bitcoin', 2020, 4, 31)

    # /coins/{id}/history
    def test_get_coin_history(self):
        """
        Uso normal.
        Faltaría probar máis casos
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/bitcoin/history?date=29-2-2020&localization=false'

        self.assertEqual(cg.get_coin_history('bitcoin', 2020, 2, 29), self.get(url))

    # /coins/{id}/market_chart
    def test_get_coin_market_chart(self):
        """
        Uso normal.
        Faltarían casos por probar.
        """

        cg = CoinGecko()


        url = self.get_url_base()+'coins/bitcoin/market_chart?vs_currency=eur&days=2&interval=daily'

        self.assertEqual(cg.get_coin_market_chart('bitcoin', 'eur', 2), self.get(url))

    # /coins/{id}/market_chart/range
    def test_get_coin_market_chart_range(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/bitcoin/market_chart/range?vs_currency=eur&from=1392577232'
        self.assertEqual(cg.get_coin_market_chart_range('bitcoin', 'eur', 1392577232), self.get(url+f'&to={time.time()}'))

        url = self.get_url_base()+'coins/bitcoin/market_chart/range?vs_currency=eur&from=1392577232&to=1422577232'
        self.assertEqual(cg.get_coin_market_chart_range('bitcoin', 'eur', 1392577232, 1422577232), self.get(url))

    # /coins/{id}/status_updates
    def test_get_coin_status_updates(self):
        """
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/bitcoin/status_updates'
        self.assertEqual(cg.get_coin_status_updates('bitcoin'), self.get(url))

        url += '?per_page=1&page=2'
        self.assertEqual(cg.get_coin_status_updates('bitcoin', 1, 2), self.get(url))

    # /coins/{id}/ohlc
    def test_get_coin_ohlc(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/bitcoin/ohlc?vs_currency=eur&days='

        self.assertEqual(cg.get_coin_ohlc('bitcoin', 'eur', 1), self.get(url+'1'))
        self.assertEqual(cg.get_coin_ohlc('bitcoin', 'eur', 0), self.get(url+'max'))

    # COINS # ------------------------------------------------------------------

    # CONTRACT -----------------------------------------------------------------

    # /coins/{id}/contract/{contract_address}
    def test_get_contract(self):
        """
        Uso normal.
        Casos por implementar.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/ethereum/contract/0xdac17f958d2ee523a2206206994597c13d831ec7'
        self.assertEqual(cg.get_contract('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7'), self.get(url))

    # /coins/{id}/contract/{contract_address}/market_chart
    def test_get_contract_market_chart(self):
        """
        Uso normal.
        Faltarían casos por implementar.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/ethereum/contract/0xdac17f958d2ee523a2206206994597c13d831ec7/?vs_currency=eur&days='

        self.assertEqual(cg.get_contract_market_chart('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7', 'eur'),
                self.get(url+'0'))

        self.assertEqual(cg.get_contract_market_chart('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7', 'eur', 1),
                self.get(url+'1'))


    # /coins/{id}/contract/{contract_address}/market_chart/range
    def test_get_contract_market_chart_range(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/ethereum/contract/0xdac17f958d2ee523a2206206994597c13d831ec7/market_chart/range'\
                '?vs_currency=eur&from=1392577232&to='

        r1 = cg.get_contract_market_chart_range('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7', 'eur', 1392577232, 1422577232)
        r2 = self.get(url+'1422577232')
        self.assertEqual(r1, r2)

        r3 = cg.get_contract_market_chart_range('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7', 'eur', 1392577232)
        r4 = self.get(url+str(time.time()))
        self.assertEqual(r3, r4)

    # CONTRACT # ---------------------------------------------------------------

    # ASSET_PLATFORMS ----------------------------------------------------------

    # /asset_platforms
    def test_get_asset_platforms(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'asset_platforms'

        self.assertEqual(cg.get_asset_platforms(), self.get(url))

    # ASSET_PLATFORMS # --------------------------------------------------------

    # CATEGORIES ---------------------------------------------------------------

    # /coins/categories/list
    def test_get_coins_categories_list(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/categories/list'

        self.assertEqual(cg.get_coins_categories_list(), self.get(url))

    # /coins/categories
    def test_get_coins_categories(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'coins/categories'

        self.assertEqual(cg.get_coins_categories(), self.get(url))

    # CATEGORIES # -------------------------------------------------------------

    # EXCHANGES ----------------------------------------------------------------

    # /exchanges
    def test_get_exchanges(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'exchanges/?per_page=250&page=1'

        self.assertEqual(cg.get_exchanges(250, 1), self.get(url))

    # /exchanges/list
    def test_get_exchanges_list(self):
        """
        Uso normal.
        Faltarían casos.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'exchanges/list'

        self.assertEqual(cg.get_exchanges_list(), self.get(url))

    # /exchanges/{id}
    def test_get_exchange(self):
        """
        Uso normal.
        """

        exchanges = ['binance']

        cg = CoinGecko()

        for exchange in exchanges:
            url = self.get_url_base()+f'exchanges/{exchange}'

            self.assertEqual(cg.get_exchange(exchange), self.get(url))

    # /exchanges/{id}
    def test_get_exchange_erro(self):
        """
        Erro
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_exchange(2)

    # /exchanges/{id}/tickers
    def test_get_exchange_tickers_erros(self):
        """
        Erros
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_exchange_tickers(1)

        with self.assertRaises(ErroTipado):
            cg.get_exchange_tickers('binance', 'bnb', True, 0, False, '')

    # /exchanges/{id}/tickers
    def test_get_exchange_tickers(self):
        """
        Uso normal
        """

        cg = CoinGecko()

        # caso base
        url = self.get_url_base()+'exchanges/binance/tickers?&order=trust_score_desc'
        self.assertEqual(cg.get_exchange_tickers('binance'), self.get(url))

        # caso 1
        url = self.get_url_base()+'exchanges/binance/tickers?coin_ids=monero&order=trust_score_desc'
        self.assertEqual(cg.get_exchange_tickers('binance', 'monero'), self.get(url))

        # caso 1 complexo
        url = self.get_url_base()+'exchanges/binance/tickers?coin_ids=monero,bitcoin,ethereum&order=trust_score_desc'
        self.assertEqual(cg.get_exchange_tickers('binance', ['mon   ero', 'bitcoin', 'ethereum']), self.get(url))

        # caso 2
        url = self.get_url_base()+'exchanges/binance/tickers?coin_ids=monero&include_exchange_logo=true&order=trust_score_desc'
        r1 = cg.get_exchange_tickers(exchange_id='binance', id_moeda='monero', exchange_logo=True)
        self.assertEqual(r1, self.get(url))

        # caso 3
        url = self.get_url_base()+'exchanges/binance/tickers?coin_ids=monero&include_exchange_logo=true'\
                '&page=2&depth=cost_to_move_up_usd&order=trust_score_desc'
        r1 = cg.get_exchange_tickers(exchange_id='binance', id_moeda='monero', exchange_logo=True, pax=2, depth='cost_to_move_up_usd')
        self.assertEqual(r1, self.get(url))

        # caso no que se metan depth e orde que non estén contemplados
        url = self.get_url_base()+'exchanges/binance/tickers?coin_ids=monero&include_exchange_logo=true'\
                '&page=2'
        r1 = cg.get_exchange_tickers(exchange_id='binance', id_moeda='monero', exchange_logo=True, pax=2, depth='algo', orde='algo')
        self.assertEqual(r1, self.get(url))

    # /exchanges/{id}/tickers/status_updates
    def test_get_exchange_tickers_status_updates_erros(self):
        """
        Erros.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_exchange_tickers_status_updates(exchange_id= 0)

    # /exchanges/{id}/tickers/status_updates
    def test_get_exchange_tickers_status_updates(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'exchanges/binance/status_updates'
        self.assertEqual(cg.get_exchange_tickers_status_updates('binance'), self.get(url))

        url = self.get_url_base()+'exchanges/binance/status_updates?per_page=0&page=0'
        self.assertEqual(cg.get_exchange_tickers_status_updates('binance'), self.get(url))

        url = self.get_url_base()+'exchanges/binance/status_updates?per_page=1&page=4'
        self.assertEqual(cg.get_exchange_tickers_status_updates('binance', xpax=1, pax=4), self.get(url))

    # /exchanges/{id}/tickers/volume_chart
    def test_get_exchange_tickers_volume_chart_erros(self):
        """
        Erros.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_exchange_tickers_volume_chart(exchange_id=0)

    # /exchanges/{id}/tickers/volume_chart
    def test_get_exchange_tickers_volume_chart(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'exchanges/binance/volume_chart?days='

        self.assertEqual(cg.get_exchange_tickers_volume_chart('binance', 1), self.get(url+'1'))
        self.assertEqual(cg.get_exchange_tickers_volume_chart('binance', 0), self.get(url+'0'))
        self.assertEqual(cg.get_exchange_tickers_volume_chart('binance', 14), self.get(url+'14'))

    # EXCHANGES # --------------------------------------------------------------

    # FINANCE ------------------------------------------------------------------
    # /finance_platforms
    def test_get_finance_platforms_erros(self):
        """
        Erros.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_finance_platforms('binance')

    # /finance_platforms
    def test_get_finance_platforms(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url0 = self.get_url_base()+'finance_platforms'
        url = self.get_url_base()+'finance_platforms?per_page=0&page=0'
        self.assertEqual(cg.get_finance_platforms(), self.get(url0), self.get(url))

        url = self.get_url_base()+'finance_platforms?per_page=2&page=3'
        self.assertEqual(cg.get_finance_platforms(xpax=2, pax=3), self.get(url))

    # /finance_products
    def test_get_finance_products_erros(self):
        """
        Erros.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_finance_products('binance')

    # /finance_products
    def test_get_finance_products(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        #url0 = self.get_url_base()+'finance_products'
        url = self.get_url_base()+'finance_products?per_page=100&page=0'
        self.assertEqual(cg.get_finance_products(), self.get(url))

        url = self.get_url_base()+'finance_products?per_page=2&page=3'
        self.assertEqual(cg.get_finance_products(xpax=2, pax=3), self.get(url))

    # FINANCE # ----------------------------------------------------------------

    # INDEXES ------------------------------------------------------------------

    '''
    # /indexes
    def test_get_indexes_erros(self):
        """
        Erros.
        """

        cg = CoinGecko()

        with self.assertRaises(ErroTipado):
            cg.get_indexes('binance')

    # /indexes
    def test_get_indexes(self):
        """
        Uso normal.
        """

        cg = CoinGecko()

        url = self.get_url_base()+'indexes?per_page=0&page=0'
        self.assertEqual(cg.get_indexes(), self.get(url))

        url = self.get_url_base()+'indexes?per_page=2&page=3'
        self.assertEqual(cg.get_indexes(xpax=2, pax=3), self.get(url))

    # /indexes/{market_id}/{id}

    # /indexes/list

    # INDEXES # ----------------------------------------------------------------

# ------------------------------------------------------------------------------




