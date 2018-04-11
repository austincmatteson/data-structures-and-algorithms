from queue import Queue


def find_maximum_value(tree):
    """Traverse and print by row."""
    q = Queue()
    temp_root = tree.root
    if temp_root is None:
        return
    max_v = temp_root.val
    q.enqueue(temp_root)
    while temp_root:
        if temp_root.left:
            q.enqueue(temp_root.left)
        if temp_root.right:
            q.enqueue(temp_root.right)
        check = q.dequeue()
        if check.val > max_v:
            max_v = check.val
        if q.front is None:
            break
        temp_root = q.front.val
    return max_v
