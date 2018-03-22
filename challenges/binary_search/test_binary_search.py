from binary_search import binary_search


def test_low():
    """find value of first index in large array"""
    assert binary_search(list(range(0xFFFFFF)), 0) == 0


def test_high():
    """find value of last index in large array"""
    assert binary_search(list(range(0xFFFFFF)), 0xFFFFFF - 1) == 0xFFFFFF - 1


def test_not_inside():
    """find value of first index not in array"""
    assert binary_search([1, 17, 34, 80, 112], 90) == -1
