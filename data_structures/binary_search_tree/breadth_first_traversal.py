from queue import Queue


def breadth_first_traversal(tree):
    """Traverse and print by row."""
    q = Queue([])
    temp_root = tree.root
    q.enqueue(temp_root)
    while temp_root:
        if temp_root.left:
            q.enqueue(temp_root.left)
        if temp_root.right:
            q.enqueue(temp_root.right)
        print('{}'.format(q.front.val.val))
        q.dequeue()
        if q.front is None:
            break
        temp_root = q.front.val
