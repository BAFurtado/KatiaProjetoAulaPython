# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 16:03:51 2022

@author: Katia C. Silva
"""

import random


def descubra_o_numero(a, b):
    """
    Jogo para descobrir o número escolhido entre 'a' e 'b'

    Parameters
    ----------
    a : int
        Valor mínimo do intervalo.
    b : int
        Valor máximo do intervalo.

    Returns
    -------
    None.

    """

    # Número escolhido aleatoriamente entre 'a' e 'b'
    selecao = random.randint(a, b)
    chute = None

    # Lista com o histórico dos números chutados pelo usuário
    lista_chutes = []

    while selecao != chute:

        # Esse é o número que o usuário vai 'chutar' a cada etapa
        msg = f'Escolha um número entre {a} e {b}: '
        chute_input = input(msg)

        # Verifica condições
        if chute_input == '':
            continue

        chute = int(chute_input)

        if chute < a or chute > b:
            print(f'O número deve estar entre {a} e {b}!')
            continue

        # Guarda na memória o histórico de chutes do usuário
        lista_chutes.append(chute)

        if selecao < chute:
            msg = f'O número {chute} é maior do que o número escolhido.'
            print(msg)
        elif selecao > chute:
            msg = f'O número {chute} é menor do que o número escolhido.'
            print(msg)

    msg = f'Parabéns, você acertou o número escolhido: {selecao}!'
    print(msg)

    num_tentativas = len(lista_chutes)
    msg = f'Você precisou de {num_tentativas} tentativas para acertar.'
    print(msg)


if __name__ == '__main__':
    descubra_o_numero(0, 100)

