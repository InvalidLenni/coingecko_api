#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/10/24 18:10:22.139504
#+ Editado:	2021/11/27 21:34:25.483348
# ------------------------------------------------------------------------------
import requests as r
import json
from typing import Optional, List, Union

from excepcions import ErroTipado
# ------------------------------------------------------------------------------
class CoinGecko:
    # class variable/atribute
    __url_base: str = 'https://api.coingecko.com/api/v3/'

    # Constructor --------------------------------------------------------------
    def __init__(self) -> None:
        # no instance variables/atributes
        pass
    # --------------------------------------------------------------------------

    # Getters ------------------------------------------------------------------
    def get_url_base(self) -> str:
        return self.__url_base
    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------
    # --------------------------------------------------------------------------

    # Máxicos ------------------------------------------------------------------
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    @staticmethod
    def check_types(lista_variables, lista_tipos):
        """
        Dada unha lista de variables e outra de tipos vai mirando que estén correctos.

        @entrada:
            lista_variables -   Requirido   -   Lista de ou variable solitaria.
            └ Lista coas variables.
            lista_tipos     -   Requirido   -   Lista de ou tipo solitario.
            └ Lista cos tipos das variables.

        @saída:
            Bool    -   Sempre
            └ Indicando se todo está correcto (True) ou se non (False)
        """

        # se as listas non teñen a mesma lonxitude algo se meteu mal
        if len(lista_variables) != len(lista_tipos):
            raise ErroTipado('As listas tenhen que ter a mesma lonxitude.')

        # se mete unha variable solitaria convírtese en lista
        if type(lista_variables) != list:
            lista_variables = [lista_variables]
        # se mete un tipo solitario convírtese en lista
        if type(lista_tipos) != list:
            lista_tipos = [lista_tipos]

        for variable, tipo in zip(lista_variables, lista_tipos):
            if type(variable) == list:
                for ele in variable:
                    if type(ele) != tipo:
                        return False
            elif type(variable) != tipo:
                return False
        return True
    # --------------------------------------------------------------------------

    # Operacións ---------------------------------------------------------------

    # PING ---------------------------------------------------------------------
    # /ping
    def ping(self) -> dict:
        """
        Pingea á api para ver se está disponhible.

        @entrada:
            Ningunha.

        @saída:
            Dicionario -   Sempre
            └ Chave "gecko_says" e contido "(V3) To the Moon!".
        """
        return json.loads(r.get(self.get_url_base()+'ping').text)
    # PING # -------------------------------------------------------------------

    # SIMPLE -------------------------------------------------------------------
    # /simple/price
    def get_price(self, ids_moedas: Union[str, List[str]], ids_moedas_vs: Union[str, List[str]],
            market_cap: Optional[bool] = False, vol24h: Optional[bool] = False,
            change24h: Optional[bool] = False, last_updated: Optional[bool] = False) -> dict:
        """
        Dadas unhas moeda/s a comparar, devolve o seu valor na/s divisa/s indicada/s.
        Permite tamén mostrar o market cap, o vol ou cambio 24h e a data de última
        actualización.

        @entrada:
            ids_moedas      -   Requirido   -   Catex, Lista de catex
            └ Identificador/es da/s moeda/s da/s que se quere obter a información.
            ids_moedas_vs   -   Requirido   -   Catex, Lista de catex
            └ Identificador/es da/s divisa/s da/s a usar.
            market_cap      -   Opcional    -   Bool
            └ Indica se se mostra o market cap para os valores de ids_moedas_vs.
            vol24h          -   Opcional    -   Bool
            └ Indica se se mostra o volumen de 24 horas para os valores de ids_moedas_vs.
            change24h       -   Opcional    -   Bool
            └ Indica se se mostra o cambio de 24 horas para os valores de ids_moedas_vs.
            last_updated    -   Opcional    -   Bool
            └ Indica se se mostra o momento de última actualización para os valores de ids_moedas_vs.

        @saída:
            Dicionario  -   Sempre
            └ Coas ids_moedas de chave e cun dicionario dos distintos valores pedidos.
        """

        if not self.check_types([ids_moedas, ids_moedas_vs, market_cap, vol24h, change24h, last_updated],
                [str, str, bool, bool, bool, bool]):
            raise ErroTipado('Cometiches un erro no tipado')

        # Se mete un str faise unha lista con el para usar join
        if type(ids_moedas) == str:
            ids_moedas = [ids_moedas]

        # Se mete un str faise unha lista con el para usar join
        if type(ids_moedas_vs) == str:
            ids_moedas_vs = [ids_moedas_vs]

        # Poño todo aqui directamente pq así aforro moitos ifs; facendo a función máis rápida
        url = self.get_url_base()+'simple/price?ids='+','.join(ids_moedas)+'&vs_currencies='+\
                ','.join(ids_moedas_vs)+'&include_market_cap='+str(market_cap).lower()+\
                '&include_24hr_vol='+str(vol24h).lower()+'&include_24hr_change='+str(change24h).lower()+\
                '&include_last_updated_at='+str(last_updated).lower()

        return json.loads(r.get(url).text)

    # /simple/token_price/{id}
    def get_token_price(self, id_moeda_base: str, contract_addresses: Union[str, List[str]],
            ids_moedas_vs: Union[str, List[str]], market_cap: Optional[bool] = False,
            vol24h: Optional[bool] = False, change24h: Optional[bool] = False,
            last_updated: Optional[bool] = False) -> dict:
        """
        Dado un ou máis contract addresses e o id da blockchain á que pertence devolve o valor
        nas distintas divisas indicadas na variable ids_moedas_vs.
        Permite tamén mostrar o market cap, o vol ou cambio 24h e a data de última
        actualización.

        @entrada:
            id_moeda_base       -   Requirido   -   Catex, Lista de catex
            └ Identificador/es da/s moeda/s da/s que se quere obter a información.
            contract_addresses  -   Requirido   -   Catex, Lista de catex
            └ Identificador/es do/s token/s da/s que se quere obter a información.
            ids_moedas_vs   -   Requirido   -   Catex, Lista de catex
            └ Identificador/es da/s divisa/s da/s a usar.
            market_cap      -   Opcional    -   Bool
            └ Indica se se mostra o market cap para os valores de ids_moedas_vs.
            vol24h          -   Opcional    -   Bool
            └ Indica se se mostra o volumen de 24 horas para os valores de ids_moedas_vs.
            change24h       -   Opcional    -   Bool
            └ Indica se se mostra o cambio de 24 horas para os valores de ids_moedas_vs.
            last_updated    -   Opcional    -   Bool
            └ Indica se se mostra o momento de última actualización para os valores de ids_moedas_vs.

        @saída:
            Dicionario  -   Sempre
            └ Coas ids_moedas de chave e cun dicionario dos distintos valores pedidos.
        """

        if not self.check_types([id_moeda_base, contract_addresses, ids_moedas_vs, market_cap,\
                vol24h, change24h, last_updated], [str, str, str, bool, bool, bool, bool]):
            raise ErroTipado('Cometiches un erro no tipado')

        # Se mete un str faise unha lista con el para usar join
        if type(contract_addresses) == str:
           contract_addresses = [contract_addresses]

        # Se mete un str faise unha lista con el para usar join
        if type(ids_moedas_vs) == str:
            ids_moedas_vs = [ids_moedas_vs]

        # Poño todo aqui directamente pq así aforro moitos ifs; facendo a función máis rápida
        url = self.get_url_base()+'simple/token_price/'+id_moeda_base+'?contract_addresses='+\
                ','.join(contract_addresses)+'&vs_currencies='+','.join(ids_moedas_vs)+\
                '&include_market_cap='+str(market_cap).lower()+'&include_24hr_vol='+str(vol24h).lower()+\
                '&include_24hr_change='+str(change24h).lower()+'&include_last_updated_at='+str(last_updated).lower()

        return json.loads(r.get(url).text)

    # /simple/supported_vs_currencies
    def get_supported_vs_currencies(self) -> List[str]:
        """
        Devolve unha lista dos ids de tódalas divisas que se poden usar para a comparativa.
        Os ids que se poden poñer en funcións como a de get_price.

        @entrada:
            Ninghunha.

        @saída:
            Lista de catexs -   Sempre
            └ Ids das moedas que se poden usar para o vs.
        """

        return json.loads(r.get(self.get_url_base()+'simple/supported_vs_currencies').text)
    # SIMPLE # -----------------------------------------------------------------

    # COINS --------------------------------------------------------------------
    # /coins/list
    def get_coins_list(self) -> List[dict]:
        """
        Lista de moedas composta por dicionarios co id, símbolo e nome.
        Ordeada por id.

        @entrada:
            Ningunha.

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as moedas de CoinGecko.
        """

        return json.loads(r.get(self.get_url_base()+'coins/list').text)

    # /coins/markets
    def get_coins_markets(self, id_moeda_vs: str, ids_moedas: Optional[Union[str, List[str]]] = '',
            categoria: Optional[str] = '', orde: Optional[Union[str, List[str]]] = 'market_cap_desc',
            xpax: Optional[int] = 250, pax: Optional[int] = 0, sparkline: Optional[bool] = False,
            cambio_prezo_porcentaxe: Optional[Union[str, List[str]]] = ['1h', '24h', '7d']):
        '''
        Función para obter os datos de mercado de tódalas moedas (prezo, maket cap, volume)

        @entrada:
            ids_moeda_vs            -   Requirido   -   Catex
            └ Identificador da moeda na que se quere obter o prezo comparativo.
            ids_moedas              -   *Opcional   -   Catex, Lista de catex
            └ Identificador/es da/s moeda/s da/s que se quere obter a información.
            categoria               -   *Opcional   -   Catex, Lista de catex
            └ Unha ou varias das mostradas en /coin/categories/list.
            orde                    -   Opcional    -   Catex, Lista de catex
            └ Indica a orde en que se queren mostrar os resultados proporcionados.
                Tan só válidos: market_cap_desc, gecko_desc, gecko_asc, market_cap_asc,
                market_cap_desc, volume_asc, volume_desc, id_asc, id_desc.
            xpax                    -   Opcional    -   Enteiro
            └ Número de resultados por páxina (entre 1 e 250).
            pax                     -   Opcional    -   Enteiro
            └ Páxina de resultados.
            sparkline               -   Opcional    -   Booleano
            └ Determina a inclusión dos datos de sparkline de 7 días.
            cambio_prezo_porcentaxe -   Opcional    -   Catex, Lista de catex
            └ Porcentaxe de cambio nos rangos permitidos: 1h, 24h, 7d, 14d, 30d, 200d, 1y.

        @saida:
            Dicionario  -   Sempre
            └ Coas ids_moedas de chave e cun dicionario dos distintos valores pedidos.
        '''

        # check de que os tipos metidos sexan correctos
        if not self.check_types([id_moeda_vs, ids_moedas, categoria, orde, xpax, pax, sparkline,\
                cambio_prezo_porcentaxe], [str, str, str, str, int, int, bool, str]):
            raise ErroTipado('Cometiches un erro no tipado')

        # se meteu ids de moedas
        if ids_moedas:
            # Se mete un str faise unha lista con el para usar join
            if type(ids_moedas) == str:
                ids_moedas = [ids_moedas]
            url_ids_moedas = '&ids='+','.join(ids_moedas)
        else:
            url_ids_moedas = ''

        # se meteu categoría
        if categoria:
            url_categoria = '&category='+categoria
        else:
            url_categoria = ''

        # Se mete un str faise unha lista con el para usar join
        if type(orde) == str:
            orde = [orde]

        # Se mete un str faise unha lista con el para usar join
        if type(cambio_prezo_porcentaxe) == str:
            cambio_prezo_porcentaxe = [cambio_prezo_porcentaxe]


        url = self.get_url_base()+'coins/markets?vs_currency='+id_moeda_vs+\
                url_ids_moedas+url_categoria+'&order='+','.join(orde)+'&per_page='+str(xpax)+\
                '&page='+str(pax)+'&sparkline='+str(sparkline).lower()+'&price_change_percentage='+\
                ','.join(cambio_prezo_porcentaxe)

        return json.loads(r.get(url).text)

    # /coins
    def get_coins(self) -> List[dict]:
        """
        Lista de moedas composta por dicionarios co id, símbolo, nome, imaxes, tempo
        bloques en minutos e informacións de mercado e prezo varias.
        Ordeada por ranking (#).

        @entrada:
            Ningunha.

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as moedas de CoinGecko.
        """

        return json.loads(r.get(self.get_url_base()+'coins').text)

    # /coins/{id}
    def get_coin(self, id_moeda: str, localization: Optional[bool] = True,
            tickers: Optional[bool] = True, market_data: Optional[bool] = True,
            community_data: Optional[bool] = True, developer_data: Optional[bool] = True,
            sparkline: Optional[bool] = False) -> dict:
        """
        Devolve unha gran cantidade de información sobre unha moeda concreta.

        @entrada:
            id_moeda        -   Requirido   -   Catex
            └ Identificador da moeda da que se quere obter a información.
            localization    -   Opcional    -   Bool
            └ Controla a mostra de todas as linguas rexionais na resposta.
            tickers         -   Opcional    -   Bool
            └ Controla a mostra dos datos de tickers (limitado a 100).
              └ "is_stale": como true cando non foi actualizado nun tempo.
              └ "is_anomaly": como true cando o prezo do ticker é outliered ó sistema de coingecko.
            market_data     -   Opcional    -   Bool
            └ Controla a mostra dos datos de mercado.
            community_data  -   Opcional    -   Bool
            └ Controla a mostra dos datos de comunidade.
            developer_data  -   Opcional    -   Bool
            └ Controla a mostra dos datos de programador.
            sparkline       -   Opcional    -   Bool
            └ Controla a inclusión dos datos da minigráfica de 7 días.

        @saída:
            Dicionario  -   Sempre
            └ Con toda a información sobre esa moeda ou co erro coa chave "error"
            e de contido unha mensaxe explicando que o id non foi atopado.
        """

        if not self.check_types([id_moeda, localization, tickers, market_data, community_data,\
                developer_data, sparkline], [str, bool, bool, bool, bool, bool, bool]):
            raise ErroTipado('Cometiches un erro no tipado')

        # Poño todo directamente porque así aforro moitos ifs e a cousa vai máis rápida
        url = self.get_url_base()+'coins/'+id_moeda+'?localization='+str(localization).lower()+\
                '&tickers='+str(tickers).lower()+'&market_data='+str(market_data).lower()+\
                '&community_data='+str(community_data).lower()+\
                '&developer_data='+str(developer_data).lower()+'&sparkline='+str(sparkline).lower()

        return json.loads(r.get(url).text)

    # /coins/{id}/tickers
    def get_coin_tickers(self):
        """
        Devolve os tickers dunha moeda (paxinado por 100 elementos).

        @entrada:
            id_moeda        -   Requirido   -   Catex
            └ Identificador da moeda da que se quere obter a información.
            ids_exchanges   -   Opcional    -   Catex, lista de catex
            └
            logo_exchange   -   Opcional    -   Catex, lista de catex
            └
            pax             -   Opcional    -   Enteiro
            └
            orde            -   Opcional    -   Catex
            └
            profundidade    -   Opcional    -   Booleano

        @saída:
            └
        """
        pass

    # /coins/{id}/history
    def get_coin_history(self):
        # xFCR
        pass

    # /coins/{id}/market_chart
    def get_coin_market_chart(self):
        # xFCR
        pass

    # /coins/{id}/market_chart/range
    def get_coin_market_chart_range(self):
        # xFCR
        pass

    # /coins/{id}/status_updates
    def get_coin_status_updates(self):
        # xFCR
        pass

    # /coins/{id}/ohlc
    def get_coin_ohlc(self):
        # xFCR
        pass
    # COINS # ------------------------------------------------------------------

    # CONTRACT -----------------------------------------------------------------
    # /coins/{id}/contract/{contract_address}
    # /coins/{id}/contract/{contract_address}/market_chart
    # /coins/{id}/contract/{contract_address}/market_chart/range
    # CONTRACT # ---------------------------------------------------------------

    # ASSET_PLATFORMS ----------------------------------------------------------
    # ASSET_PLATFORMS # --------------------------------------------------------

    # CATEGORIES ---------------------------------------------------------------
    # /coins/categories/list
    def get_coins_categories_list(self):
        """
        Devolve todas as categorías cd CG nunha lista de dics compostos
        por id e nome.

        @entrada:
            Ningunha.

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as categorías de CoinGecko
        """

        return json.loads(r.get(self.get_url_base()+'coins/categories/list').text)

    # /coins/categories
    def get_coins_categories(self):
        """
        Devolve unha lista de todas as categorías de CG con datos de mercado asociados.

        @entrada:
            Ningunha.

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as categorías de CoinGecko con datos de mercado
        """

        return json.loads(r.get(self.get_url_base()+'coins/categories').text)
    # CATEGORIES # -------------------------------------------------------------

    # EXCHANGES ----------------------------------------------------------------
    # EXCHANGES # --------------------------------------------------------------

    # FINANCE ------------------------------------------------------------------
    # FINANCE # ----------------------------------------------------------------

    # INDEXES ------------------------------------------------------------------
    # INDEXES # ----------------------------------------------------------------

    # DERIVATIVES --------------------------------------------------------------
    # DERIVATIVES # ------------------------------------------------------------

    # STATUS_UPDATES -----------------------------------------------------------
    # STATUS_UPDATES # ---------------------------------------------------------

    # EVENTS -------------------------------------------------------------------
    # EVENTS # -----------------------------------------------------------------

    # EXCHANGE_RATES -----------------------------------------------------------
    # EXCHANGE_RATES # ---------------------------------------------------------

    # TRENDING -----------------------------------------------------------------
    # TRENDING # ---------------------------------------------------------------

    # GLOBAL -------------------------------------------------------------------
    # GLOBAL # -----------------------------------------------------------------

    # COMPANIES ----------------------------------------------------------------
    # COMPANIES # --------------------------------------------------------------

    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------
def main():
    # import aki para non sobre importar se se usa como módulo
    from uteis.imprimir import jprint

    cg = CoinGecko()

    # TESTS --------------------------------------------------------------------

    # /ping
    #jprint(cg.ping())

    # --------------------------------------------------------------------------

    # /simple/price
    #jprint(cg.get_price('bitcoin', 'eur'))
    #jprint(cg.get_price(['bitcoin', 'ethereum'], ['eur', 'usd']))

    # /simple/token_price/{id}
    # tether e whackd
    #jprint(cg.get_token_price('ethereum', '0xdac17f958d2ee523a2206206994597c13d831ec7,0xCF8335727B776d190f9D15a54E6B9B9348439eEE', 'eur,usd'))
    # gooddollar
    #jprint(cg.get_token_price('ethereum', '0x67C5870b4A41D4Ebef24d2456547A03F1f3e094B', 'eur,usd'))

    # /simple/supported_vs_currencies
    #jprint(cg.get_supported_vs_currencies())

    # --------------------------------------------------------------------------

    # /coins/list
    #jprint(cg.get_coins_list()[1329])

    # /coins/markets
    #jprint(cg.get_coins_markets('usd', ids_moedas = ['bitcoin', 'ethereum']))
    #jprint(cg.get_coins_markets('usd', ids_moedas = 'bitcoin'))
    #jprint(cg.get_coins_markets('usd', categoria = 'aave-tokens'))
    #jprint(cg.get_coins_markets('usd', categoria = 'analytics'))
    # xFCR

    # /coins
    #jprint(cg.get_coins()[0]['id'])

    # /coins/{id}
    #jprint(cg.get_coin('bitcoin'))

    # /coins/{id}/tickers
    # /coins/{id}/history
    # /coins/{id}/market_chart
    # /coins/{id}/market_chart/range
    # /coins/{id}/status_updates
    # /coins/{id}/ohlc

    # TESTS # ------------------------------------------------------------------

    # CATEGORIES ---------------------------------------------------------------
    # /coins/categories/list
    #jprint(cg.get_coins_categories_list())

    # /coins/categories
    #jprint(cg.get_coins_categories())
    # CATEGORIES # -------------------------------------------------------------


if __name__=='__main__':
    main()
# ------------------------------------------------------------------------------
