from task6_5 import number_in_the_fibonacci


def test_number_in_the_fibonacci():
    assert number_in_the_fibonacci(1) == 0
    assert number_in_the_fibonacci(2) == 1
    assert number_in_the_fibonacci(3) == 1
    assert number_in_the_fibonacci(4) == 2
    assert number_in_the_fibonacci(5) == 3
    assert number_in_the_fibonacci(6) == 5
    assert number_in_the_fibonacci(7) == 8
    assert number_in_the_fibonacci(8) == 13
    assert number_in_the_fibonacci(9) == 21
    assert number_in_the_fibonacci(10) == 34
