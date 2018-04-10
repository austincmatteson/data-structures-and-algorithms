def _fizzbuzz(node):
    """Fizzbuzz helper function."""
    if node.val % 15 == 0:
        node.val = 'fizzbuzz'
    elif node.val % 3 == 0:
        node.val = 'fizz'
    elif node.val % 5 == 0:
        node.val = 'buzz'
    return node


def fizz_buzz_tree(tree):
    """Fizzbuzz traversal."""
    tree.in_order(_fizzbuzz)
    return tree
