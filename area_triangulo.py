"""Define a área de um triângulo"""


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


if __name__ == '__main__':
    resultado = area_triangulo(5, 10)
    print(f'A área do triângulo é:{resultado}')
