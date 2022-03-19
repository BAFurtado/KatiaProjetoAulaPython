"""
Retira os duplicados de uma lista
"""

# def remove_duplicados(mylist: list) -> list:
#
#     res = list(set(mylist))
#     return res


def remove_duplicados(mylist: list) -> list:

    lista_ndup = []
    for i in mylist:
        if i not in lista_ndup:
            lista_ndup.append(i)
    return lista_ndup


if __name__ == '__main__':

    res = remove_duplicados([1, 2, 2, 3, 4])
    print(res)
