from task5_5 import get_ranges


def test_get_ranges():
    assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4, 7-8, 10"
    assert get_ranges([4, 7, 10]) == "4, 7, 10"
    assert get_ranges([2, 3, 8, 9]) == "2-3, 8-9"
