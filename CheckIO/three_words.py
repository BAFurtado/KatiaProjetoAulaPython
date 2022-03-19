

def checkio(words: str) -> bool:

    resultado = words.split(' ')

    if len(resultado) < 3:
        return False

    for index in range(len(resultado) - 2):
        palavra1 = resultado[index]
        palavra2 = resultado[index + 1]
        palavra3 = resultado[index + 2]

        if palavra1.isalpha() and palavra2.isalpha() and palavra3.isalpha():
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")