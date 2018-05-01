from hash_table import HashTable as HT


def repeated_word(string):
    """."""
    try:
        all_words = string.lower().split(' ')
    except TypeError:
        raise TypeError
    ht = HT()
    for each in all_words:
        found = ht.get(each)
        if found:
            return each
        ht.set(each, each)
