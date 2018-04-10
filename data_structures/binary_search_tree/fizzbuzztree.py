import bst


def _fizzbuzz(node):
    if node.val % 15 == 0:
        node.val = 'fizzbuzz'
    elif node.val % 3 == 0:
        node.val = 'fizz'
    elif node.val % 5 == 0:
        node.val = 'buzz'
    return node


def fizz_buzz_tree(tree):
    tree.in_order(_fizzbuzz)
    return tree


a = bst.BST()
a.insert(10)
a.insert(5)
a.insert(3)
a.insert(6)
a.insert(15)
a.insert(11)
a.insert(16)
a.in_order(lambda n: print(n.val))
fizz_buzz_tree(a)
a.in_order(lambda n: print(n.val))
