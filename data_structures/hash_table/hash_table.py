from functools import reduce
from linked_list import LinkedList as LL


class HashTable:
    """."""

    def __init__(self, max_size=1024):
        """."""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def _hash_key(self, key):
        """."""
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """Insert into hash table."""
        return self.buckets[self._hash_key(key)].insert({key: val})

    def get(self, key, filter=None):
        """."""
        current = self.buckets[self._hash_key(key)].head
        while current:
            if key in current.val.keys():
                return current.val[key]
            current = current._next

    def remove(self, key):
        """."""
        start = self.buckets[self._hash_key(key)]
        current = start.head
        while current:
            removed, current = current.val, current._next
            start.head = current
            return removed
