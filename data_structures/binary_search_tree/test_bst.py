from fizzbuzztree import fizz_buzz_tree


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
