"""
Тесты
"""
import sorting
import pytest


DEFAULT_LIST = [3, 1, 4, 5, 2]
EMPTY = []
NEGATIVE_LIST = [3, -1, 4, 5, -2]
NONVALID_LIST = [3, 'one', 4, 5, '-2']


def test_bubble_smoke():
    test_list = DEFAULT_LIST
    result = sorting.bubble_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_bubble_empty():
    test_list = EMPTY
    result = sorting.bubble_sort(test_list)
    assert result ==[]


def test_bubble_negative():
     test_list = NEGATIVE_LIST
     result = sorting.bubble_sort(test_list)
     test_list.sort()
     assert result == test_list


def test_bubble_not_integer():
    test_list = NONVALID_LIST
    with pytest.raises(RuntimeError):
        sorting.bubble_sort(test_list)
        

def test_insert_smoke():
    test_list = DEFAULT_LIST
    result = sorting.insert_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_insert_empty():
    test_list = EMPTY
    result = sorting.insert_sort(test_list)
    assert result ==[]


def test_insert_negative():
     test_list = NEGATIVE_LIST
     result = sorting.insert_sort(test_list)
     test_list.sort()
     assert result == test_list


def test_insert_not_integer():
    test_list = NONVALID_LIST
    with pytest.raises(RuntimeError):
        sorting.insert_sort(test_list)


def test_selection_smoke():
    test_list = DEFAULT_LIST
    result = sorting.selection_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_selection_empty():
    test_list = EMPTY
    result = sorting.selection_sort(test_list)
    assert result == []


def test_selection_negative():
    test_list = NEGATIVE_LIST
    result = sorting.selection_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_selection_not_integer():
    test_list = NONVALID_LIST
    with pytest.raises(RuntimeError):
        sorting.selection_sort(test_list)


