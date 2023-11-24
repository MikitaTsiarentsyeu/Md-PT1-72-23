from task6_2 import is_a_palindrome


def test_is_a_palindrome():
    assert is_a_palindrome('мадам') == True
    assert is_a_palindrome('дед') == True
    assert is_a_palindrome('1178711') == True
    assert is_a_palindrome('peep') == True
    assert is_a_palindrome('Saippuakivikauppias') == True
    assert is_a_palindrome('а роза упала на лапу Азора') == True
    assert is_a_palindrome('Я — арка края') == True
    assert is_a_palindrome(
        'Муза, ранясь шилом опыта, ты помолишься на разум'
    ) == True
    assert is_a_palindrome(
        'Муха! О, муха! Велика аки лев! Ах, ум! О ах, ум!'
    ) == True
    assert is_a_palindrome('Madam, I’m Adam') == True
    assert is_a_palindrome('') == False
    assert is_a_palindrome('M') == False
    assert is_a_palindrome('\t  \n  \t') == False
    assert is_a_palindrome(',M,') == False
    assert is_a_palindrome('General Electric GE') == False
    assert is_a_palindrome('90') == False
    assert is_a_palindrome('3404') == False
    assert is_a_palindrome('8,14') == False
