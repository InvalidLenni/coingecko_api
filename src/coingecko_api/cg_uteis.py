#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/04 14:01:43.443863
#+ Editado:	2021/12/04 15:12:07.340154
# ------------------------------------------------------------------------------
from datetime import datetime

from typing import Optional
# ------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------
def e_bisesto(ano):
    """
    Identifica un ano como bisiesto ou non.

    @entrada:
        ano -   Requirido   -   Int.
        └ Ano a clasificar.

    @saída:
        Bool    -   Sempre
        └ Indicando se é bisiesto (True) ou non (False).
    """
    div4 = ano%4 == 0
    div100 = ano%100 == 0
    div400 = ano%400 == 0

    return div4 and (not div100 or div400)
# ------------------------------------------------------------------------------
def unix2human(unix_ts: int, sep_d: Optional[str] = '/', sep_h: Optional[str] = ':'):
    """
    Data unha data en unix como int devolve a data correctamente formatada

    @entrada:
        unix_ts -   Requirido   -   Int
        └ Data en formato unix.
        sep_d   -   Requirido   -   Catex
        └ O que se quere mostrar para separar aaaa mm dd.
        sep_h   -   Requirido   -   Catex
        └ O que se quere mostrar para separar hh mm ss.

    @saída:
        Catex   -   Sempre
        └ Coa data formatada en formato lexible por humanos.
    """

    return datetime.fromtimestamp(int(str(unix_ts)[:10])).strftime(f'%Y{sep_d}%m{sep_d}%d %H{sep_h}%M{sep_h}%S')
# ------------------------------------------------------------------------------
def main():
    print('Executando os uteis de coingecko directamente')
    print(unix2human(1638536400000, '-', ':'))

if __name__ == '__main__':
    main()
