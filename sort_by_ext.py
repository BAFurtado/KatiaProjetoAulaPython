from typing import List


def sort_by_ext(files: List[str]) -> List[str]:

    # Modulo do Python que trabalha com caminhos de arquivos
    # ImportError: The module `os` is not allowed on checkio.
    # import os
    import re
    import pandas as pd

    # os.path.splitext('.config')
    # os.path.splitext('config.')
    # os.path.splitext('table.imp.xls')
    # os.path.splitext('.imp.xls')

    re.match(r'^(.+?)\.?(.+?)$', '.config')
    re.match(r'^(.+?)\.?(.+?)$', 'config.')
    re.match(r'^(.+?)\.?(.+?)$', 'table.imp.xls')
    re.match(r'^(.+?)\.?(.+?)$', '.imp.xls')

    lst_nome_arquivo = []
    lst_extensao = []

    for itens in files:

        if itens.endswith('.'):
            nome_arquivo = itens
            extensao = ''
        else:
            nome_arquivo, extensao = os.path.splitext(itens)

        lst_nome_arquivo.append(nome_arquivo)
        lst_extensao.append(extensao.replace('.', ''))

    # Cria um DataFrame para ordenar o nome dos arquivos
    df = pd.DataFrame()
    df['files'] = pd.Series(files)
    df['extensao'] = pd.Series(lst_extensao)

    df = df.sort_values(['extensao', 'files'])
    resultado = df['files'].tolist()

    return resultado


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
