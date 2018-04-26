from k_tree import KTree as K
from print_level_order import print_level_order as plo
from find_matches import find_matches as fm
import sys
import pytest


def test_breadth(capsys, tree):
    """Correct output order."""
    tree.breadth_first_traversal(lambda n: print(n.__str__()))
    sys.stderr.write("10\n5\n3\n6\nmeow\n15\n11\n")
    out, err = capsys.readouterr()
    assert out == err


def test_breadth_empty(capsys):
    """Correct empty ouput."""
    a = K()
    a.breadth_first_traversal(lambda n: print(n.__str__()))
    sys.stderr.write("")
    out, err = capsys.readouterr()
    assert out == err


def test_breadth_no_operation(capsys):
    """Raise error if missing lambda."""
    a = K()
    with pytest.raises(TypeError):
        assert a.breadth_first_traversal()


def test_pre(capsys, tree):
    """Correct output order."""
    tree.pre_order(lambda n: print(n.__str__()))
    sys.stderr.write("10\n5\n3\n6\n15\n11\nmeow\n")
    out, err = capsys.readouterr()
    assert out == err


def test_pre_empty(capsys):
    """Correct empty ouput."""
    a = K()
    a.pre_order(lambda n: print(n.__str__()))
    sys.stderr.write("")
    out, err = capsys.readouterr()
    assert out == err


def test_pre_no_operation(capsys):
    """Raise error if missing lambda."""
    a = K()
    with pytest.raises(TypeError):
        assert a.pre_order()


def test_post(capsys, tree):
    """Correct output order."""
    tree.post_order(lambda n: print(n.__str__()))
    sys.stderr.write("5\n3\n11\n15\n6\nmeow\n10\n")
    out, err = capsys.readouterr()
    assert out == err


def test_post_empty(capsys):
    """Correct empty ouput."""
    a = K()
    a.post_order(lambda n: print(n.__str__()))
    sys.stderr.write("")
    out, err = capsys.readouterr()
    assert out == err


def test_post_no_operation(capsys):
    """Raise error if missing lambda."""
    a = K()
    with pytest.raises(TypeError):
        assert a.post_order()


def test_insert_wrong_parent(capsys, tree):
    """Raise error if parent does not exist."""
    tree.insert(4, 100)
    tree.breadth_first_traversal(lambda n: print(n.__str__()))
    sys.stderr.write("10\n5\n3\n6\nmeow\n15\n11\n")
    out, err = capsys.readouterr()
    assert out == err


def test_insert_no_parent(tree):
    """Raise error if missing lambda."""
    with pytest.raises(ValueError):
        assert tree.insert(1)


def test_insert_no_value(tree):
    """Raise error if missing lambda."""
    with pytest.raises(TypeError):
        assert tree.insert()


def test_repr(tree):
    """Return correct format."""
    assert type(tree.__repr__()) is str


def test_str(tree):
    """Return correct format."""
    assert type(tree.__str__()) is int


def test_node(tree):
    """Return correct format."""
    assert type(tree.root.__repr__()) is str


def test_plo(tree):
    """Correct output."""
    assert plo(tree) == '10\n536meow\n15\n11'


def test_plo_empty():
    """No nodes."""
    k = K()
    with pytest.raises(AttributeError):
        assert plo(k)


def test_plo_single(tree):
    """No children."""
    k = K()
    k.insert(1)
    assert plo(k) == '1'


def test_matches_none(tree):
    """No matches."""
    assert fm(tree, 300) == []


def test_matches_one(tree):
    """One match."""
    test = fm(tree, 'meow')
    assert len(test) == 1
    assert test[0].val == 'meow'


def test_matches_many():
    """All matches."""
    k = K()
    k.insert(1)
    k.insert(2, 1)
    k.insert(2, 1)
    k.insert(2, 1)
    k = fm(k, 2)
    for each in k:
        assert each.val == 2
