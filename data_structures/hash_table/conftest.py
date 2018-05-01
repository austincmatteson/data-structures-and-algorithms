from hash_table import HashTable as HT
import pytest


@pytest.fixture
def hash_test():
    """Test hash table."""
    ht = HT()
    ht.set('meow', 1)
    ht.set('woof', 2)
    ht.set('blammo', 3)
    return ht
