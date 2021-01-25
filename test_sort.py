"""
Тесты
"""
import sorting


def test_bubble():
    test_list = [3, 1, 4, 5, 2]
    result = sorting.bubble_sort(test_list)
    assert result == [1, 2, 3, 4, 5]
