def backward_string_by_word(text: str) -> str:
    # your code here

    a = ''
    res = text.replace(" ", " _ ")
    resultado = res.split(" ")

    for index in range(len(resultado)):
        palavra1 = resultado[index]
        for i in range(len(palavra1) - 1, -1, -1):
            el = palavra1[i]
            a = a + el
            a = a.replace("_"," ")
    return a


if __name__ == '__main__':
    print('hello   world')
    print(backward_string_by_word('hello   world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
