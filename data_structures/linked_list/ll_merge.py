def merge_lists(LL1, LL2):
    """Merge two lists."""
    current1 = LL1.head
    current2 = LL2.head
    while not current1:
        return LL2.head
    while current1 and current2:
        temp = current2._next
        if not current1._next:
            current1._next = current2
            break
        current2._next = current1._next
        current1._next = current2
        current1 = current2._next
        current2 = temp
    return LL1.head
