li = ['kiwi', 'eagle', 'sparrow', 'pigeon', 'hawk']
def reverse_list(li):
    '''This function takes a list, reverse its items and return a new list'''
    res = []
    for i in li:
        res.append(i[::-1])
    return res

print(reverse_list(li))