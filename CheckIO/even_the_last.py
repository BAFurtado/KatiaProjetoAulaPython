def checkio(lista: list) -> int:
    """
        sums even-indexes elements and multiply at the last
        :type array: object
    """

    contador = 0

    if len(lista) != 0:
        for index in range(len(lista)):
            if index % 2 == 0:
                contador += lista[index]
                resultado = contador * lista[-1]
    else:
        resultado = 0

    return resultado


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
