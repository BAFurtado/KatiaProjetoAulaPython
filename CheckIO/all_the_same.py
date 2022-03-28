from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    # Se for vazio, então os elementos são iguais
    if len(elements) == 0:
        return True

    # Se todos os itens forem iguais ao primeiro, então são todos iguais
    else:

        # Forma de resolução de programadores avançados, usando list comprehension
        # lista_comparacao = [True if item == elements[0] else False for item in elements]

        # Forma de resolução de programadores iniciantes
        # lista_comparacao = []
        # for item in elements:
        #     if item == elements[0]:
        #         lista_comparacao.append(True)
        #     else:
        #         lista_comparacao.append(False)
        #
        # # A função all() verifica se todos os elementos são verdadeiros
        # return all(lista_comparacao)

        all_same = True
        for item in elements:
            if item != elements[0]:
                all_same = False
        return all_same

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
