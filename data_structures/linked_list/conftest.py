import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def empty_ll():
    """Empty linked list for use with tests."""
    return LL()


@pytest.fixture
def predefined_ll():
    """Default linked list for use with tests."""
    return LL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
