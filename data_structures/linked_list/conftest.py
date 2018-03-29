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


@pytest.fixture
def predefined_ll_other():
    """Second linked list for use with tests."""
    return LL([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


@pytest.fixture
def predefined_ll_short():
    """Shorter linked list for use with tests."""
    return LL([11, 12, 13, 14])
