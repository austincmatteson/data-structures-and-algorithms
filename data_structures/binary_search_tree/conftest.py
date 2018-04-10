import pytest
from bst import BST


@pytest.fixture
def tree():
    """Instantiate tree."""
    a = BST()
    a.insert(10)
    a.insert(5)
    a.insert(3)
    a.insert(6)
    a.insert(15)
    a.insert(11)
    a.insert(16)
    return a
