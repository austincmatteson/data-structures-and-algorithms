from queue import Queue


class Animal_Shelter:
    """Queue with value reference."""
    def __init__(self):
        """Accept dogs and cats."""
        self.animal = ['dog', 'cat']
        self.q = Queue([])

    def enqueue(self, animal):
        """Add dog or cat."""
        if animal in self.animal:
            self.q.enqueue(animal)
            return self.q.back.val
        raise TypeError('must be dog or cat')

    def dequeue(self, pref=None):
        """Remove dog or cat or first."""
        if pref in self.animal or pref is None:
            current = self.q.front
            adopt = None
            if pref is None or pref.lower() == current.val:
                return self.q.dequeue()
            while current._next:
                if current._next.val == pref.lower():
                    adopt = current._next
                    current._next = current._next._next
                    self.q._size -= 1
                    return adopt.val
                current = current._next
            print('None currently in shelter.')
            return adopt
        raise TypeError('must be dog or cat')
