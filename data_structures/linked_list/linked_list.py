from node import Node


class LinkedList:
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

        try:
            for item in reversed(iter):
                self.insert(item)
        except TypeError:
            print('Not an iterable')

    def __str__(self):
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        start = self.head
        while start:
            if start.val == val:
                return True
            start = start._next
        return False

    def append(self, val):
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(val)

    def insert_before(self, val, new_val):
        current = self.head
        while current._next.val != val:
            current = current._next
        current._next = Node(new_val, current._next)

    def insert_after(self, val, new_val):
        current = self.head
        while current.val != val:
            current = current._next
        current._next = Node(new_val, current._next)
