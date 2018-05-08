import pytest
from selection import selection_sort as ss
from mergesort import mergesort as ms


def test_selection_sorted():
    """Return self."""
    assert ss([]) == []
    assert ss([1]) == [1]
    assert ss([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_selection_random():
    """Return sorted from random."""
    assert ss([300, 2, 5, 86, 7, 1, 543, 17]) == [1, 2, 5, 7, 17, 86, 300, 543]


def test_selection_nonlist():
    """Raise error."""
    with pytest.raises(TypeError):
        assert ss(5)
        assert ss('meow')


def test_merge_sorted():
    """Return self."""
    assert ms([]) == []
    assert ms([1]) == [1]
    assert ms([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_random():
    """Return sorted from random."""
    assert ms([300, 2, 5, 86, 7, 1, 543, 17]) == [1, 2, 5, 7, 17, 86, 300, 543]


def test_merge_nonlist():
    """Raise error."""
    with pytest.raises(TypeError):
        assert ms(5)
        assert ms('meow')
