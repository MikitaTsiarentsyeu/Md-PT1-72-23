from task6_1 import reverse_a_string


def test_reverse_a_string():
    assert reverse_a_string('Hello, World!') == '!dlroW ,olleH'
    assert reverse_a_string('-5, 6') == '6 ,5-'
    assert reverse_a_string('$!%^&4') == ('4&^%!$')
    assert reverse_a_string('   ') == '   '
    assert reverse_a_string('') == ''
