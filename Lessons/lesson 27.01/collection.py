class StackWithIteration:

    def __init__(self, *items) -> None:
        self.__items = []
        if items:
            self.__items.extend(items)

    def push(self, item):
        self.__items.insert(0, item)

    def pop(self):
        return self.__items.pop(0)
    
    def __str__(self) -> str:
        return f"{StackWithIteration.__name__}({','.join([str(x) for x in self.__items])})"

    def __len__(self):
        return len(self.__items)
    
    def __add__(self, other):
        if isinstance(other, StackWithIteration):
            return StackWithIteration(*self.__items+list(other))
        
    def __iter__(self):
        # return iter(self.__items)
        self.__iteration_index = 0
        return self

    def __next__(self):
        if self.__iteration_index >= len(self.__items):
            del self.__iteration_index
            raise StopIteration
        else:
            item = self.__items[self.__iteration_index]
            self.__iteration_index += 1
            return item
        
    def __getitem__(self, key):
        try:
            return self.__items[key]
        except IndexError:
            raise IndexError(f"{StackWithIteration.__name__} index out of range")
    
    def __setitem__(self, key, value):
        try:
            self.__items[key] = value
        except IndexError:
            self.push(value)

st = StackWithIteration()
st.push(1)
st.push(2)
st.push(3)
print(st)
print(st.pop())
print(st)
print(len(st))
print(list(st))

for i in st:
    print(i)

print(StackWithIteration(1,2,3)+StackWithIteration(4,5,6))

st = StackWithIteration(1,2,3,4,5,6)
print(st[0])
st[4] = 5.00005
print(st[4])
st[10] = 11
print(st)