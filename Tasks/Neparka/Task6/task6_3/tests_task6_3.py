from task6_3 import count_of_occurrences


def test_count_of_occurrences():
    assert count_of_occurrences('', 'a') == 0
    assert count_of_occurrences('Hello', 'a') == 0
    assert count_of_occurrences('Hello, World!', 'a') == 0
    assert count_of_occurrences('Hello, World!', 'l') == 3
    assert count_of_occurrences('Hello, World!', 'o') == 2
    assert count_of_occurrences('Hello, World!', ',') == 1
