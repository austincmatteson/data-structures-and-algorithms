from largest_product import largest_product
import pytest


def test_highest():
    """Work as expected."""
    assert largest_product([[1, 2], [3, 7], [5, 8], [6, 3]]) == 56


def test_multiple():
    """Pass in larger array."""
    assert largest_product([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]) == 72


def test_negative():
    """Test with negative values."""
    assert largest_product([[-1, 2], [-3, 4], [-5, 6], [-7, 8]]) == 35


def test_negative2():
    """Find even if largest is negative."""
    assert largest_product([[-1, 1], [7, -1]]) == -1


def test_non_list():
    """Must pass in list."""
    with pytest.raises(TypeError) as err:
        largest_product(2)
    assert str(err.value) == 'Argument(s) invalid.'


def test_non_list_of_list():
    """Must pass in list of lists."""
    with pytest.raises(TypeError) as err:
        largest_product([1, 2])
    assert str(err.value) == 'Argument(s) invalid.'


def test_non_2d():
    """Must pass in 2d list."""
    with pytest.raises(TypeError) as err:
        largest_product([[1, 2], [1, 2], [1, 2, 3]])
    assert str(err.value) == 'Argument(s) invalid.'


def test_non_int():
    """Must pass in 2d list of ints."""
    with pytest.raises(TypeError) as err:
        largest_product([[1, 2], [1, 'a']])
    assert str(err.value) == 'Argument(s) invalid.'
