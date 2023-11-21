# 1. Write a recursive function to reverse a string.
def reverse_str(string, counter=1, res=[]):
    if (1 or 0) == len(string):
        return string
    if counter != len(string) - 1:
        counter += 1
        counter = reverse_str(string, counter)
    res.append(string[counter])
    counter = counter - 1
    return counter

print(reverse_str('spy'))

# self.assertEqual(recursion.reverse_str('wow'), 'wow')
#         self.assertEqual(recursion.reverse_str(''), '')
#         self.assertEqual(recursion.reverse_str('yes'), 'sey')
#         self.assertEqual(recursion.reverse_str('ZaRiNa'), 'aNiRaZ')
#         self.assertEqual(recursion.reverse_str(' '), ' ')
#         self.assertEqual(recursion.reverse_str('123'), '321')