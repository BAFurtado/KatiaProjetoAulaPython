
def nearest_value(values: set, one: int) -> int:

    import math

    lista = list(values)

    minima_distancia = math.inf
    item_menor_distancia = None

    for item in lista:

        distancia = abs(item - one)

        if distancia < minima_distancia:
            minima_distancia = distancia
            item_menor_distancia = item

        elif distancia == minima_distancia:
            if item_menor_distancia > item:
                item_menor_distancia = item

    return item_menor_distancia


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")