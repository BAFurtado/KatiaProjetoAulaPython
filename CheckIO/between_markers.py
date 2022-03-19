def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    primeira_particao = text.partition(begin)
    segunda_particao = primeira_particao[2].partition(end)
    palavra = segunda_particao[0]

    return palavra


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is ><', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')