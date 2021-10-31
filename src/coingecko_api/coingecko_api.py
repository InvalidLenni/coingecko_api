#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/10/24 18:10:22.139504
#+ Editado:	2021/10/31 19:06:05.307838
# ------------------------------------------------------------------------------
import requests as r
import json
from typing import List
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
    def get_coin(self, id_moeda: str) -> dict:
        """
        Devolve unha gran cantidade de información sobre unha moeda concreta.

        @entrada:
            id_moeda    -   Requirido   -   Catex
            └ Identificador da moeda da que se quere obter a información.

        @saída:
            Dicionario  -   Sempre
            └ Con toda a información sobre esa moeda ou co erro coa chave "error"
            e de contido unha mensaxe explicando que o id non foi atopado.
        """
        return json.loads(r.get(self.get_url_base()+'coins/'+id_moeda).text)

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

if __name__=='__main__':
    main()
# ------------------------------------------------------------------------------

