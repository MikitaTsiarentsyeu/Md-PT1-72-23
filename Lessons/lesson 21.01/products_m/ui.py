import dl_bl

class UI_Manager:

    @staticmethod
    def get_all():
        try:
            products = dl_bl.get_all()
        except:
            print("something went wrong, please try again")
        if products:
            for p in products:
                print(p)
        else:
            print("no products")

    @staticmethod
    def create():
        params = input("Enter the product name, descr, price comma separated\n")
        try:
            p = dl_bl.create(params)
        except:
            print("something went wrong, please try again")
        print(f"new product was created - {p}")
        
    @staticmethod
    def validate_id():
        while True:
            id = input("Enter the integer product id\n")
            try:
                id = int(id)
            except ValueError:
                print("the value should be integer")
                continue
            break
        return id

    @staticmethod
    def get():
        id = UI_Manager.validate_id()
        try:
            p = dl_bl.get(id)
        except:
            print("something went wrong, please try again")
        if p:
            print(f"the product was found - {p}")
        else:
            print("nothing was found") 

    @staticmethod
    def delete():
        id = UI_Manager.validate_id()
        try:
            d = dl_bl.delete(id)
        except:
            print("something went wrong, please try again")
        if d:
            print(f"the product with {id} was deleted")
        else:
            print("nothing was found")

    @classmethod
    def main_loop(cls):
        while True:
            print("Choose an number of the menu item from the list below:\n")
            print("0. Exit")
            print("1. Get all products")
            print("2. Create a product")
            print("3. Get a product by id")
            print("4. Delete a product by id")
            answ = input()
            if answ == '0':
                break
            elif answ == '1':
                cls.get_all()
            elif answ == '2':
                cls.create()
            elif answ == '3':
                cls.get()
            elif answ == '4':
                cls.delete()
            else:
                print("wrong input")


if __name__ == "__main__":
    UI_Manager.main_loop()