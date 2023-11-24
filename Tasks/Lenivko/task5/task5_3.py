li = ['BMW', 'Mercedes-Benz', 'Volvo', 'Lada', 'Honda', 'Mini', 'Toyota', 'Zaz', 'Lotus', 'KIA', 'Opel']

def li_item_len(li):
    '''This function takes a list and returns a new list of items with max length more than 5'''
    res = []
    for i in li:
        if len(i) > 5:
            res.append(i)
        else:
            continue
    return res

print(li_item_len(li))