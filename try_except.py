
x = '1212s'

try:
    meu_numero = int(x)
except Exception as erro:
    print(f'Deu ruim. Erro {erro}')
finally:
    print('Função executou belezinha!')


def is_numeric(x):
    try:
        float(x)
        return True
    except:
        return False


is_numeric('12.1223')
is_numeric('12.1223x')

