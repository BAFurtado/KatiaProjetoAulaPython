
import datetime as dt


def days_diff(a, b):

    # O asterisco (*) aqui funciona como um 'unpack' da lista,
    # no qual o primeiro elemento da lista irá se tornar o primeiro argumento da função,
    # o segundo elemento da lista irá se tornar o segundo argumento da função
    # e assim por diante.

    dt1 = dt.date(*a)
    dt2 = dt.date(*b)

    # Diferença entre as datas, em dias.

    date_diff = dt2 - dt1
    resposta = abs(date_diff.days)

    return resposta


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
