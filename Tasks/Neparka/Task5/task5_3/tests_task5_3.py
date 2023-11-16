from task5_3 import strings_greater_than_5


def test_strings_greater_than_5():
    assert strings_greater_than_5(
        ['Hi', 'hello', 'welcome', 'home', 'see you later']
    ) == ['welcome', 'see you later']
    assert strings_greater_than_5(
        ['-5', '65', '123', '4567', '891011']
    ) == ['891011']
    assert strings_greater_than_5(
        ['', ' ', '   ', '    ', '     ', '      ', '       ']
    ) == ['      ', '       ']
    assert strings_greater_than_5(
        ['! @  #', '*  & ^', '!@#$%^&*']
    ) == ['! @  #', '*  & ^', '!@#$%^&*']
    assert strings_greater_than_5([]) == []
    assert strings_greater_than_5(['Hi', 'hello']) == []
