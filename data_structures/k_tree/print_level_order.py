from q import Q


def print_level_order(tree):
    """Print tree values by depth."""
    q = Q()
    q2 = Q()
    q.enqueue(tree.root)
    container = ''
    while q or q2:
        if not q:
            q, q2 = q2, q
            container += '\n'
        node = q.dequeue()
        for child in node.children:
            q2.enqueue(child)
        container += str(node.val)
    return container
