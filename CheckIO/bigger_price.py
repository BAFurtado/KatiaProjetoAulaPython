
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """

    # Cria uma lista com os preços dos produtos (que estão no dicionário)
    lista_preco = []
    for item in data:
        lista_preco.append(item["price"])

    # Ordena a lista do maior para o menor
    lista_preco.sort(reverse=True)

    # Seleciona os 'limits' maiores preços
    preco_maior = lista_preco[0:limit]

    # Para cada preço procura o dicionário correspondente e adiciona a uma lista de resultado
    resultado = []
    for preco in preco_maior:
        for item in data:
            if preco == item['price']:
                resultado.append(item)

    return resultado


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')