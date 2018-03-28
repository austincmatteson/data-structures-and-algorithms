from node import Node


class LinkedList:
    """Linked list data structure"""
    def __init__(self, iter=[]):
        """Initialize linked list of size length."""
        self.head = None
        self._size = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            raise TypeError('Please pass an iterable.')

    def __str__(self):
        """Return current head value."""
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        """Return current list length."""
        return self._size

    def insert(self, val):
        """Insert value at start of list."""
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        """Find value if exists."""
        start = self.head
        while start:
            if start.val == val:
                return True
            start = start._next
        return False

    def append(self, val):
        """Append value to end of list."""
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(val)

    def insert_before(self, val, new_val):
        """Insert new value before specified value in list."""
        current = self.head
        while current._next.val != val:
            current = current._next
        current._next = Node(new_val, current._next)

    def insert_after(self, val, new_val):
        """Insert new value after specified value in list."""
        current = self.head
        while current.val != val:
            current = current._next
        current._next = Node(new_val, current._next)

    def kth_from_end(self, k):
        """Find kth value from end of list."""
        current = self.head
        counter = self._size - 1 - k
        if (counter < 0) | (counter >= self._size):
            raise ValueError
        while counter > 0:
            current = current._next
            counter -= 1
        return current.val
