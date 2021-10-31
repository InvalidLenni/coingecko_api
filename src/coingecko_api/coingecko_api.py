#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/10/24 18:10:22.139504
#+ Editado:	2021/10/31 17:35:32.373654
# ------------------------------------------------------------------------------
import requests
import json
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
    def ping(self):
        """
        Pingea á api para ver se está disponhible.

        @entrada:
            Ningunha.

        @saída:
            Dicionario -   Sempre
            └ Chave "gecko_says" e contido "(V3) To the Moon!".
        """
        return json.loads(requests.get(self.get_url_base()+'ping').text)

    # /coins
    def get_coins(self):
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
        return json.loads(requests.get(self.get_url_base()+'coins').text)

    # /coins/list
    def get_coins_list(self):
        """
        Lista de moedas composta por dicionarios co id, símbolo e nome.
        Ordeada por id.

        @entrada:

        @saída:
            Lista de dicionarios   -   Sempre
            └ Todas as moedas de CoinGecko.
        """
        return json.loads(requests.get(self.get_url_base()+'coins/list').text)
    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------
def main():
    cg = CoinGecko()
    #print(cg.ping())
    #print(cg.get_coins()[0]['id'])
    #print(cg.get_coins_list()[1329])

if __name__=='__main__':
    main()
# ------------------------------------------------------------------------------

