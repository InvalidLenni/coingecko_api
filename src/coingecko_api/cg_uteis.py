#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/04 14:01:43.443863
#+ Editado:	2021/12/04 14:13:35.023285
# ------------------------------------------------------------------------------

from datetime import datetime

from typing import Optional

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

def main():
    print('Executando os uteis de coingecko directamente')
    print(unix2human(1638536400000, '-', ':'))

if __name__ == '__main__':
    main()
