from towers_of_hanoi import towers_of_hanoi as t


def test_empty():
    """Test passing no discs means no gameplay."""
    empty = t(0)
    assert not empty[0] and not empty[1] and not empty[2]


def test_small_moved():
    """Test final state solved."""
    smallest = t(1)
    smaller = t(2)
    small = t(3)
    norm = t(4)
    assert not smallest[0] and not smallest[1] and smallest[2] == [1]
    assert not smaller[0] and not smaller[1] and smaller[2] == [2, 1]
    assert not small[0] and not small[1] and small[2] == [3, 2, 1]
    assert not norm[0] and not norm[1] and norm[2] == [4, 3, 2, 1]


def test_efficiency():
    """Test solved per (2^n)-1 algorithm for lowest move count."""
    assert not t(0)[3]              # none
    assert t(1)[3] == 2 ** 1 - 1    # 1
    assert t(2)[3] == 2 ** 2 - 1    # 3
    assert t(3)[3] == 2 ** 3 - 1    # 7
    assert t(10)[3] == 2 ** 10 - 1  # 1023
