import pytest
from linked_list import LinkedList as LL


def test_insert_first_node(empty_ll):
    """Test insert to start of linked list."""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_find_an_int_in_ll(predefined_ll):
    """Test find in linked list."""
    assert predefined_ll.find(1) is True
    assert predefined_ll.find(11) is False


def test_noniterable_as_argument():
    """Test raises correct error when passed noniterable."""
    with pytest.raises(TypeError) as err:
        LL(1234)
    assert str(err.value) == 'Please pass an iterable.'


def test_append(predefined_ll):
    """Test append to end of list."""
    assert predefined_ll.find(11) is False
    predefined_ll.append(11)
    assert (predefined_ll.head._next._next._next._next._next._next._next._next
            ._next._next.val) == 11


def test_before(predefined_ll):
    """Test insert before without breaking link."""
    assert predefined_ll.find(11) is False
    predefined_ll.insert_before(5, 11)
    assert (predefined_ll.head._next._next._next._next.val) == 11
    assert (predefined_ll.head._next._next._next._next._next.val) == 5
    assert (predefined_ll.head._next._next._next._next._next._next.val) == 6


def test_after(predefined_ll):
    """Test insert after without breaking link."""
    assert predefined_ll.find(11) is False
    predefined_ll.insert_after(5, 11)
    assert (predefined_ll.head._next._next._next._next.val) == 5
    assert (predefined_ll.head._next._next._next._next._next.val) == 11
    assert (predefined_ll.head._next._next._next._next._next._next.val) == 6


def test_kth_from_end(predefined_ll):
    """Test kth from end exists."""
    assert predefined_ll.kth_from_end(2) == 8
    assert predefined_ll.kth_from_end(0) == 10
    assert predefined_ll.kth_from_end(9) == 1


def test_kth_from_end_break(predefined_ll):
    """Test kth from end wrong passes."""
    with pytest.raises(ValueError):
        predefined_ll.kth_from_end(10)
        predefined_ll.kth_from_end(-1)
    with pytest.raises(TypeError):
        predefined_ll.kth_from_end('a')
