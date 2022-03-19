"""
Identifica se uma letra é vogal ou consoante
"""


def vogal(a):

    lista_vogal = ['a', 'e', 'i', 'o', 'u']
    lista_consoante = list('bcdfghjklmnpqrstvwxyz')

    if a.lower() in lista_vogal:
        print(f'A letra {a} é uma vogal.')
    elif a.lower() in lista_consoante:
        print(f'A letra {a} é uma consoante.')
    else:
        print(f'Você não digitou uma letra.')


if __name__ == '__main__':

    vogal('a')
    vogal('B')
    vogal('1')
    vogal('z')

