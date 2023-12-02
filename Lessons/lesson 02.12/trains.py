class FreightTrain:

    CART_LEN = 120

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self):
        return f"I'm a train of {self.cart_count} carts, choo-choo!"
    
    def __len__(self):
        return self.cart_count*FreightTrain.CART_LEN
    
    def __int__(self):
        return self.cart_count
    
    def __eq__(self, o):
        if isinstance(o, FreightTrain):
            return self.cart_count == o.cart_count
        
        if isinstance(o, int):
            return self.cart_count == o
        
        return False
        
    def add(self, o):
        if not isinstance(o, FreightTrain):
            return False
        
        return FreightTrain(self.cart_count + o.cart_count)

f = FreightTrain(5)
print(str(f), len(f), int(f))
len(f)

long = FreightTrain(100)
shorty = FreightTrain(10)
print(long == long, long == shorty, long == 100)
print(long == 100)
print(100 == long)


print(long+shorty)