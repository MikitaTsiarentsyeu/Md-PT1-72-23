from task6_4 import the_power


def test_the_power():
    assert the_power(10, 0) == 1
    assert the_power(10, -1) == 0.1
    assert the_power(10, -4) == 0.0001
    assert the_power(10, 3) == 1000
    assert the_power(-10, 3) == -1000
    assert the_power(-10, 4) == 10000
    assert the_power(81, 1/4) == 3
    assert the_power(-81, 1/4) == 'Не определяется.'
    assert the_power(10, -0.12) == 0.7585775750291838
    assert the_power(-10, -0.12) == 'Не определяется.'
    assert the_power(7, 3) == 343
    assert the_power(2, 19) == 524288
    assert the_power(2, -3) == 0.125
    assert the_power(0, -3) == 0
