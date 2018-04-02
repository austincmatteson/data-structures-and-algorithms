class Node:
    """Node pointer for linked list."""

    def __init__(self, val, next=None):
        """Intialize node."""
        self.val = val
        self._next = next

    def __str__(self):
        """Return value as string."""
        return '{val}'.format(val=self.val)
