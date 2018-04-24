class Q:
    """Queue data structure."""
    class Node:
        """Node pointer for linked list."""
        def __init__(self, val, next=None):
            """Intialize node."""
            self.val = val
            self._next = next

        def __str__(self):
            """Return value as string."""
            return '{val}'.format(val=self.val)

    def __init__(self, iter=[]):
        """Intialize queue."""
        self.front = None
        self.back = None
        self._size = 0

        try:
            for item in iter:
                self.enqueue(item)
        except TypeError:
            raise TypeError('Please pass an iterable.')

    def __str__(self):
        """Return current front value."""
        return '<front> => {}\n<back> => {}'.format(self.front.val, self.back
                                                    .val)

    def __len__(self):
        """Return current stack length."""
        return self._size

    def enqueue(self, val):
        """Push new value into back of queue."""
        eq = self.Node(val)
        if not self.front:
            self.front = eq
            self.back = self.front
            self._size += 1
            return self.front
        else:
            self.back._next = eq
            self.back = eq
            self._size += 1
            return self.back

    def dequeue(self):
        """Pop value from front of queue."""
        if self._size == 0:
            print('Queue is empty.')
        else:
            dq = self.front
            self.front = self.front._next
            self._size -= 1
            return dq.val
