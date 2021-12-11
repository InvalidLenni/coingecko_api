#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/04 14:01:43.443863
#+ Editado:	2021/12/11 20:52:58.195474
# ------------------------------------------------------------------------------
from datetime import datetime

from src.coingecko_api.excepcions import ErroTipado

from typing import Optional
# ------------------------------------------------------------------------------
def check_types(varis, tipos):
    """
    Dada unha lista de variables e outra de tipos vai mirando que estén correctos.

    @entrada:
        varis    -   Requirido   -   Lista de ou variable solitaria.
        └ Lista coas variables.
        tipos   -   Requirido   -   Lista de ou tipo solitario.
        └ Lista cos tipos das variables.

    @saída:
        Bool    -   Sempre
        └ Indicando se todo está correcto (True) ou se non (False)
    """

    # se mete unha variable solitaria convírtese en lista
    if type(varis) != list:
        varis = [varis]

    # se mete un tipo solitario convírtese en lista
    if type(tipos) != list:
        tipos = [tipos]

    # para que o caso especial de [] e [list] dé que son iguais
    # vaise que [] sexa [list] para que logo de que list == list
    if (not varis) and (len(tipos) == 1 and tipos[0] == list):
        varis = [list]

    # se as listas non teñen a mesma lonxitude algo se meteu mal
    if len(varis) != len(tipos):
        raise ErroTipado('As listas tenhen que ter a mesma lonxitude.')

    # recorrer as listas
    for var, tipo in zip(varis, tipos):
        # só var porque list (en tipo) non é type list senón type
        if type(var) == list:
            if not check_types(var, tipo):
                return False
        # mira que o tipo ou o propio contido non sexan igual ó tipo
        elif (type(var) != tipo) and (var != tipo):
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
    div4   = ano%4 == 0
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
