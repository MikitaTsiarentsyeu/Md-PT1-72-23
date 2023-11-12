l = [4,5,6,3,12,3,5,8,8,6,4]

target = 8

def linear_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return False

print(linear_search(l, target))



def search(l, target, low=0, high=None):
    high = len(l)-1 if high == None else high

    if low > high:
        return False

    mid = (low + high) // 2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return search(l, target, low, mid-1)
    else:
        return search(l, target, mid+1, high)
    
l = [1,2,3,4,5]

print(search(l, -11))