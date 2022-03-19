

ano_nasc = 1980

lista = []
for numero in range(ano_nasc, 2702):
    if numero % 7 == 0 and numero % 13 == 0:
        lista.append(numero)

print(lista)
