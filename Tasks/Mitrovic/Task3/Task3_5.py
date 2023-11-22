my_lst = ['I', 'would', 'like', 'to', 'go', 'to', 'the', 'cinema', 'on', 'Saturday', 'and',
          'I', 'would', 'like', 'to', 'go', 'to', 'London', 'on', 'Sunday']
my_new_lst = []
for i in my_lst:
    if len(i) > 5:
        my_new_lst.append(i)
print(my_new_lst)
