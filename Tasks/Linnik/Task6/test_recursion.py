import unittest
import recursion


class TestRecursion(unittest.TestCase):

    def test_reverse_str(self):
        self.assertEqual(recursion.reverse_str('wow'), 'wow')
        self.assertEqual(recursion.reverse_str(''), '')
        self.assertEqual(recursion.reverse_str('yes'), 'sey')
        self.assertEqual(recursion.reverse_str('ZaRiNa'), 'aNiRaZ')
        self.assertEqual(recursion.reverse_str(' '), ' ')
        self.assertEqual(recursion.reverse_str('123'), '321')

    def test_palindrome(self):
        self.assertTrue(recursion.palindrome('wow'))
        self.assertTrue(recursion.palindrome('k'))
        self.assertTrue(recursion.palindrome(''))
        self.assertFalse(recursion.palindrome('key'))

    def test_num_letter(self):
        self.assertEqual(recursion.num_letter('a', 'Alana'), 2)
        self.assertEqual(recursion.num_letter('b', 'bobb'), 3)
        self.assertEqual(recursion.num_letter('O', 'Olow'), 1)
        self.assertEqual(recursion.num_letter('4', '2344544'), 4)

    def test_pow_num(self):
        self.assertEqual(recursion.pow_num(4, 4), 256)
        self.assertEqual(recursion.pow_num(3, 3), 27)
        self.assertEqual(recursion.pow_num(2, 2), 4)
        self.assertEqual(recursion.pow_num(1, 1), 1)
        self.assertEqual(recursion.pow_num(0, 0), 1)
        self.assertEqual(recursion.pow_num(2, -1), 0.5)

    def test_fibonacci(self):
        # 0, 1, 1, 2, 3, 5, 8, 13, 21
        self.assertEqual(recursion.fibonacci(1), 0)
        self.assertEqual(recursion.fibonacci(3), 1)
        self.assertEqual(recursion.fibonacci(5), 3)
        self.assertEqual(recursion.fibonacci(8), 13)
        self.assertEqual(recursion.fibonacci(9), 21)
