import pandas as pd

def frequency_sort(items):

    df = pd.DataFrame()
    df['items'] = pd.Series(items, dtype=object)
    df['row_number'] = df.index

    df['freq'] = df.groupby(['items'])['items'].transform('count')
    df['first'] = df.groupby(['items'])['row_number'].transform('first')
    df = df.sort_values(['freq', 'first'], ascending=[False, True])

    lista = df['items'].tolist()

    return lista


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")