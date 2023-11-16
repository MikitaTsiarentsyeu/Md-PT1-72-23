from task5_2 import strings_mirroring


def test_strings_mirroring():
    assert strings_mirroring(['Hi', 'hello']) == ['iH', 'olleh']
    assert strings_mirroring(['-5', '65']) == ['5-', '56']
    assert strings_mirroring(['', ' ']) == ['', ' ']
    assert strings_mirroring(['! @  #', '*  & ^']) == ['#  @ !', '^ &  *']
    assert strings_mirroring([]) == []
