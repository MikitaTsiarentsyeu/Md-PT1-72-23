import json
import random

class Product_Id_Index:

    __id_index = {0}

    def get_new_id(self):
        id = 0
        while id in Product_Id_Index.__id_index:
            id = random.randint(1000, 9999)
        else:
            Product.Product_Id_Index.add(id)
        return

class Product:

    def __init__(self, name, descr, price) -> None:
        self.id = Product_Id_Index.get_new_id()
        self.name = name
        self.descr = descr
        self.price = price

    def from_str(self): pass

    def from_dict(self): pass

    def __str__(self) -> str:
        pass

    def to_dict(self):
        d = {}
        d["id"] = self.id
        d["name"] = self.name
        d["descr"] = self.descr
        d["price"] = self.price
        return d
    
p = Product("test name", "test descr", 90)
print(p.to_dict())

def get_all(): pass

def create(params): pass

def get(id): pass

def delete(id): pass