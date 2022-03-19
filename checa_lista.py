"""
Escreva um programa que, dada uma lista qualquer, retorna: o primeiro valor, o número de valores, o último valor,
a soma, a média
"""

def confere_lista(mylist):

    primeiro_elemento = mylist[0]
    print(f'O primeiro elemento da lista é {primeiro_elemento}.')

    tamanho = len(mylist)
    print(f'A lista possui {tamanho} elementos.')

    ultimo_elemento = mylist[tamanho - 1]
    print(f'O último elemento da lista é: {ultimo_elemento}')

    soma = sum(mylist)
    print(f'A soma dos elementos da lista é igual a: {soma}.')

    media = soma / tamanho
    print(f'A média é igual a {media}.')


if __name__ == '__main__':

    mylist = [1, 3, 5, 6]
    confere_lista(mylist)