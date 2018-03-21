import shift_array
import pytest


def test_pass_even():
    assert shift_array.insertShiftArray([1, 2, 3, 4], 5) == [1, 2, 5, 3, 4]


def test_pass_even_odd():
    assert shift_array.insertShiftArray([1, 2, 3], 4) == [1, 2, 4, 3]


def test_fail():
    with pytest.raises(TypeError) as err:
        shift_array.insertShiftArray(1, 'a')
    assert str(err.value) == 'Argument(s) invalid.'
