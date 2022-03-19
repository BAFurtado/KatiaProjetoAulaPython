

for numero in range(1, 51):

    oopsdoh = ''

    if numero % 3 == 0:
        oopsdoh = oopsdoh + 'Oops'

    if numero % 5 == 0:
        oopsdoh = oopsdoh + 'Doo'

    print(f'Numero {numero}: {oopsdoh}')

