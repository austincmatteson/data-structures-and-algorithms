import pytest
from k_tree import KTree


@pytest.fixture
def tree():
    """Instantiate tree."""
    a = KTree()
    a.insert(10)
    a.insert(5, 10)
    a.insert(3, 10)
    a.insert(6, 10)
    a.insert(15, 6)
    a.insert(11, 15)
    a.insert('meow', 10)
    return a
