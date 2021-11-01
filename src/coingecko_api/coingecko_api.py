#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/10/24 18:10:22.139504
#+ Editado:	2021/11/01 16:16:42.720272
# ------------------------------------------------------------------------------
import requests as r
import json
from typing import Optional, List, Union
# ------------------------------------------------------------------------------
class CoinGecko:
    __url_base: str = 'https://api.coingecko.com/api/v3/'

    # Constructor --------------------------------------------------------------
    def __init__(self) -> None:
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

    # Operacións ---------------------------------------------------------------
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
            └ Controla a mostra dos datos de tickers.
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
        # Poño todo directamente porque así aforro moitos ifs e a cousa vai máis rápida
        url = self.get_url_base()+'coins/'+id_moeda+'?localization='+str(localization).lower()+\
                '&tickers='+str(tickers).lower()+'&market_data='+str(market_data).lower()+\
                '&community_data='+str(community_data).lower()+\
                '&developer_data='+str(developer_data).lower()+'&sparkline='+str(sparkline).lower()

        return json.loads(r.get(url).text)

    # /coins/list
    def get_coins_list(self) -> List[dict]:
        """
        Lista de moedas composta por dicionarios co id, símbolo e nome.
        Ordeada por id.

        @entrada:

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as moedas de CoinGecko.
        """
        return json.loads(r.get(self.get_url_base()+'coins/list').text)
    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------
def main():
    cg = CoinGecko()

    #print(cg.ping())

    #print(cg.get_coins()[0]['id'])

    #print(cg.get_coins_list()[1329])

    #print(cg.get_coin('bitcoin'))

    print(cg.get_price('bitcoin', 'eur'))
    print(cg.get_price(['bitcoin', 'ethereum'], ['eur', 'usd']))

if __name__=='__main__':
    main()
# ------------------------------------------------------------------------------
