import json
import random

class Product:

    class __Product_Id_Index:

        @staticmethod
        def get_new_id():
            id = 0
            with open('products_m/index.txt', 'r') as f:
                indexes = f.read().split(',')
            while str(id) in indexes:
                id = random.randint(1000, 9999)
            else:
                with open('products_m/index.txt', 'a') as f:
                    f.write(f",{id}")
            
            return id

    def __init__(self, name, descr, price, id=False) -> None:
        if id:
            self.id = id
        else:
            # self.id = 1
            self.id = self.__Product_Id_Index.get_new_id()
        self.name = name
        self.descr = descr
        self.price = price

    @classmethod
    def from_str(cls, str_product):
        attrs = [x.strip() for x in str_product.split(',')]
        return cls(attrs[0], attrs[1], attrs[2])

    @classmethod
    def from_dict(cls, dict_product):
        return cls(dict_product['name'], dict_product['descr'], dict_product['price'], dict_product['id'])

    def __str__(self) -> str:
        return f"{self.id}: {self.name}, {self.descr}, {self.price}"

    def to_dict(self):
        d = {}
        d["id"] = self.id
        d["name"] = self.name
        d["descr"] = self.descr
        d["price"] = self.price
        return d
    
class Product_Manager:

    @staticmethod
    def read_products():
        with open("products_m/products.json", 'r') as f:
            return json.load(f)
        
    @staticmethod
    def write_products(products):
        with open("products_m/products.json", 'w') as f:
            json.dump(products, f)

    @staticmethod
    def create(product_str):
        product = Product.from_str(product_str)
        products = Product_Manager.read_products()
        
        products.append(product.to_dict())
        Product_Manager.write_products(products)
        return product

    @staticmethod
    def get(id):
        products = Product_Manager.read_products()

        for p in products:
            if p['id'] == id:
                return str(Product.from_dict(p))
        return False
    
    @staticmethod
    def get_all():
        products = [str(Product.from_dict(p)) for p in Product_Manager.read_products()]
        return products

    @staticmethod
    def delete(id):
        products = Product_Manager.read_products()

        for i, p in enumerate(products):
            if p['id'] == id:
                break
        else:
            return False
        
        del products[i]
        Product_Manager.write_products(products)
        return True

def get_all():
    return Product_Manager.get_all()

def create(product_str):
    return Product_Manager.create(product_str)

def get(id):
    return Product_Manager.get(id)

def delete(id):
    return Product_Manager.delete(id)