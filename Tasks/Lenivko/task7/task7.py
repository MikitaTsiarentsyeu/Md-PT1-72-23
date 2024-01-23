import re

class Book:
    def __init__(self, title, author, isbn, price):
        self.__title = title
        self.__author = author
        self.__set_isbn(isbn)
        self.__price = price
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
        
    def get_author(self):
        return self.__author
    
    def set_title(self, author):
        self.__author = author
        
    def get_isbn(self):
        return self.__isbn
    
    def __set_isbn(self, isbn):
        if len(str(isbn)) != 13:
            return 'Incorrect ISBN. Please check the number and try again.'
        self.__isbn = isbn
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
        
    
class EBook(Book):
    __formats = ["pdf", "txt", "epub"]
    __default_format = 0    
    def __init__(self, title, author, isbn, price, format, file_size, download_link):
        super().__init__(title, author, isbn, price)
        self.set_format(format)
        self.file_size = file_size
        self.set_download_link(download_link)
    
    def set_format(self, format):
        if format in EBook.__formats:
            self.__format = format
        else:
            self.__format = EBook.__formats[EBook.__default_format]
        
    def get_download_link(self):
        return self.__download_link
    
    def set_download_link(self, download_link):
        if download_link.startswith('https://'):
            self.__download_link = download_link
        else:
            return f'https://{download_link}'
        
class PhysicalBook(Book):
    def __init__(self, title, author, isbn, price, weight):
        super().__init__(title, author, isbn, price)
        self.weight = weight
        self.in_stock = True
        
    def check_in_stock(self):
        if self.in_stock:
            return ("В наличии.")
        else:
            self.in_stock = False
            return ("Нет в наличии.")
            
        
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class ShoppingCart:
    def __init__(self):
        self.chosen_books = []
        self.purchase_amount = 0
        
    def add__book(self, chosen_book):
        chosen_book.title.append(self.chosen_books)
        self.purchase_amount += chosen_book.price
    
    def get_chosen_books(self):
        return self.chosen_books
    
    def get_purchase_amount(self):
        return self.purchase_amount
    
class PremiumCustomer(Customer):
    __member_status = 'Premium'
    __DISCOUNT = 10
    
    def __init__(self, name, email, address, status, discount):
        super().__init__(name, email, address)
        self.set__status(status)
        self.set_discount(discount)
        
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
        
    def get_discount(self):
        return self.__discount
    
    def set_discount(self, discount):
        if self.status == PremiumCustomer.__member_status:
            self.__discount = f'{PremiumCustomer.__DISCOUNT} %'
        else:
            self.__discount = 0
    
    def apply_discount(self, purchase_amount, discount):
        return purchase_amount - ((purchase_amount / 100) * discount)
    
    
class Order:
    def __init__(self, buyer, order_info):
        self.buyer = buyer
        self.order_info = ShoppingCart.self.chosen_books
        self.total_price = ShoppingCart.self.purchase_amount
        self.set_finally_price(finally_price)
        
    def get_buyer(self):
        return self.buyer
        
    def get_order_info(self):
        return self.order_info
    
    def get_total_price(self):
        return self.total_price
    
    def set_finally_price(self, buyer, total_price):
        if buyer == PremiumCustomer.get_status:
            finally_price = PremiumCustomer.apply_discount(total_price)
        else:
            finally_price = ShoppingCart.self.purchase_amount
            
    def get_finally_price(self):
        return self.finally_price