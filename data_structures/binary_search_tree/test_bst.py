from fizzbuzztree import fizz_buzz_tree
from breadth_first_traversal import breadth_first_traversal
from find_maximum_value_binary_tree import find_maximum_value
from bst import BST
import sys


def test_fizz(tree):
    """Fizz when divisible by 3."""
    assert tree.root.left.left.val == 3
    assert fizz_buzz_tree(tree).root.left.left.val == 'fizz'


def test_buzz(tree):
    """Buzz when divisible by 5."""
    assert tree.root.val == 10
    assert fizz_buzz_tree(tree).root.val == 'buzz'


def test_fizzbuzz(tree):
    """Fizzbuzz when divisible by 3 and 5."""
    assert tree.root.right.val == 15
    assert fizz_buzz_tree(tree).root.right.val == 'fizzbuzz'


def test_no_fizzbuzz(tree):
    """Skip when not divisible by 3 or 5."""
    assert tree.root.right.left.val == 11
    assert fizz_buzz_tree(tree).root.right.left.val == 11


def test_breadth(capsys, tree):
    """Correct output order."""
    breadth_first_traversal(tree)
    sys.stderr.write("10\n5\n15\n3\n6\n11\n16\n")
    out, err = capsys.readouterr()
    assert out == err


def test_breadth_unbalanced(capsys, tree):
    """Correct output order."""
    tree.insert(4)
    breadth_first_traversal(tree)
    sys.stderr.write("10\n5\n15\n3\n6\n11\n16\n4\n")
    out, err = capsys.readouterr()
    assert out == err


def test_breadth_none(capsys):
    """No output."""
    a = BST()
    breadth_first_traversal(a)
    sys.stderr.write("")
    out, err = capsys.readouterr()
    assert out == err


def test_max(tree):
    """Correct output order."""
    assert find_maximum_value(tree) == 16


def test_max_unbalanced(tree):
    """Correct output order."""
    tree.insert(4)
    assert find_maximum_value(tree) == 16


def test_max_none(capsys):
    """No output."""
    a = BST()
    assert find_maximum_value(a) is None
