

def split_pairs(a):

    lista = []

    if len(a) % 2 != 0:
        a = a + '_'

    # Percorre a lista de 2 em 2
    for i in range(0, len(a), 2):
        index1 = i
        index2 = i + 2
        lista.append(a[index1:index2])

    return lista


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcdesd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")