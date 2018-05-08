import pytest
from selection import selection_sort as ss


def test_selection_sorted():
    """Return self."""
    assert ss([]) == []
    assert ss([1]) == [1]


def test_selection_random():
    """Return sorted from random."""
    assert ss([300, 2, 5, 86, 7, 1, 543, 17]) == [1, 2, 5, 7, 17, 86, 300, 543]


def test_selection_nonlist():
    """Raise error."""
    with pytest.raises(TypeError):
        assert ss(5)
        assert ss('meow')
