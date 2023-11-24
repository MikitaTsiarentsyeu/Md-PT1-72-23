from task5_4 import case_counter


def test_case_counter():
    assert case_counter('Write a function') == (13, 1)
    assert case_counter('that takes') == (9, 0)
    assert case_counter('') == (0, 0)
    assert case_counter('A STRING') == (0, 7)
    assert case_counter('12123 $%^& as an argument AND') == (12, 3)
    assert case_counter(['12123 $%^&']) == (0, 0)
