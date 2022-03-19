"""Avalia o tamanho da senha"""


def is_acceptable_password(password: str) -> bool:
    check = len(password)
    if check > 6:
        return True
    else:
        return False


if __name__ == '__main__':
    res = is_acceptable_password('a')
    print(f'A resposta é {res}')
