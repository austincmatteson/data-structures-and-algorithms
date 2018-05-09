import pytest
from selection import selection_sort as ss
from mergesort import mergesort as ms
from quicksort import quick_sort as qs


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


def test_quick_sorted():
    """Return self."""
    assert qs([]) == []
    assert qs([1]) == [1]
    assert qs([1, 2, 3]) == [1, 2, 3]


def test_quick_random():
    """Return sorted from random."""
    assert qs([34, 19, 42, -9, 2018, 0, 2005, 77, 2099]) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_quick_nonlist():
    """Raise error."""
    with pytest.raises(TypeError):
        assert qs(5)
        assert qs('meow')
