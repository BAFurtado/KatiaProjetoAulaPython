
def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """

    # Cria um dicionário vazio
    freq_words = {}

    # Eu usei o get para evitar erro de 'key' inexistente. Quando a 'Key' for inexistente, a função
    for item in data:
        freq_words[item] = freq_words.get(item, 0) + 1

    maximo = max(freq_words.values())

    letra_maximo = ''
    for (chave, valor) in freq_words.items():
        if valor == maximo:
            letra_maximo = chave

    # lista_str = []
    # lista_contador = []
    #
    # for i in range(len(data)):
    #     marcador = 0
    #     string1 = data[i]
    #
    #     # Evita calcular várias vezes o número de ocorrências
    #     # da mesma string
    #     if string1 in lista_str:
    #         continue
    #
    #     for j in range(len(data)):
    #         string2 = data[j]
    #         if string1 == string2:
    #             marcador = marcador + 1
    #
    #     lista_str.append(string1)
    #     lista_contador.append(marcador)
    #
    # maximo = max(lista_contador)
    # indice_maximo = lista_contador.index(maximo)
    # letra_maximo = lista_str[indice_maximo]

    return letra_maximo


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
