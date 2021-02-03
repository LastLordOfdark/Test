"""
Тесты
"""
import sorting
import pytest
from random import randint

RANGE = 1000


def rand_gen(amount: int) -> list:
    return [randint(- RANGE, RANGE) for _ in range(amount)]


DEFAULT_LIST = rand_gen(10)
EMPTY_LIST = []
NEGATIVE_LIST = [3, -1, 4, 5, -2]
NONVALID_LIST = [3, 'one', 4, 5, '-2']


@pytest.mark.parametrize("test_list", [DEFAULT_LIST, NEGATIVE_LIST])
@pytest.mark.parametrize("test_func", [sorting.bubble_sort,
                                       sorting.selection_sort,
                                       sorting.insert_sort])
def test_all(test_list, test_func):
    result = test_func(test_list)
    assert result == sorted(test_list)


@pytest.mark.parametrize("test_list", [NONVALID_LIST,
                                       EMPTY_LIST])
@pytest.mark.parametrize("test_func", [sorting.bubble_sort,
                                       sorting.selection_sort,
                                       sorting.insert_sort])
def test_selection_not_integer(test_list, test_func):
    test_list = test_list
    with pytest.raises(RuntimeError):
        test_func(test_list)
