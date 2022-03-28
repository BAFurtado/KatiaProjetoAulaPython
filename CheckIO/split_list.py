
def split_list(items: list) -> list:

    items_len = len(items)

    if items_len % 2 == 0:
        first_half_index = int(items_len/2)
        res = [items[0:first_half_index], items[first_half_index:items_len]]
    else:
        first_half_index = int(items_len/2) + 1
        res = [items[0:first_half_index], items[first_half_index:items_len]]

    # your code here
    return res


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
