from task5_1 import sum_of_two_ints


def test_sum_of_two_ints():
    assert sum_of_two_ints(-5, -6) == -11
    assert sum_of_two_ints(-5, 6) == 1
    assert sum_of_two_ints(5, -6) == -1
    assert sum_of_two_ints(5, 6) == 11
    assert sum_of_two_ints(5, 0) == 5
    assert sum_of_two_ints(0, 6) == 6
    assert sum_of_two_ints(0, 0) == 0
    assert sum_of_two_ints(0, -0) == 0
    assert sum_of_two_ints(-0, -0) == 0
