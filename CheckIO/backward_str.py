def backward_string(val: str) -> str:
    # your code here
    a = ''
    for i in range(len(val) - 1, -1, -1):
        el = val[i]
        a = a + el
    return a


if __name__ == '__main__':

    print(backward_string('fabio'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")