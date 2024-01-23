class Book:
    def __init__(self, title, author, ISBN, price):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__price = price

    def __set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title
    def __set_author(self, author):
        self.__author = author
    def get_author(self):
        return self.__author
    def __set_ISBN(self, ISBN):
        if len(__ISBN) == 13:
            self.__ISBN = ISBN
        else:
            print("Error, the ISBN isn't a 13-digit number!")
    def get_ISBN(self):
        return self.__ISBN

    def __set_price(self):
        if self.__price >= 0:
            self.__price = price
        else:
            print("Error, the price can't be < 0")
    def get_price(self):
        return self.__price

    __book_title = property(get_title)
    __book_author = property(get_author)
    __book_ISBN = property(get_ISBN, __set_ISBN)
    __book_price = property(get_price, __set_price)

book_1 = Book('best of 1980', 'Bykau', 1111111111111, 10)
book_2 = Book('best of 1990', 'Aleksievich', 2222222222222, 20)
book_3 = Book('best of 2000', 'Arlou', 3333333333333, 30)

class EBook(Book):

    __FORMATS = ['pdf', 'epub', 'fb2', 'mobi', 'kf8', 'txt', 'doc', 'docx']

    def __init__(self, format, file_size, download_link, title, author, ISBN, price):
        super().__init__(title, author, ISBN, price)
        self.__format = format
        self.file_size = file_size
        self.__download_link = download_link
    def __set_format(self, format):
        if self.format in Ebook.__FORMATS:
            self.__format = format
        else:
            print("This format isn't in the list of supported formats")
    def get_format(self):
        return self.__format
    def set_file_size(self):
        if self.file_size >= 0:
            return self.file_size == file_size
        else:
            print("Error, the file_size can't be < 0")
    def get_file_size(self):
        return self.file_size

    def set_download_link(self, some_link):
        if some_link[0:8] == 'https://':
            self.__download_link = some_link
        else:
            print("Error, the link must be started with 'https://'")
    def get_download_link(self):
        return self.__download_link

    format = property(get_format, __set_format)
    download_link = property(get_download_link)


e_book_1 = EBook('pdf', '30', 'https://mybooks/ebook1.com', 'best of 1980', 'Bykau', 1111111111111, 10)
e_book_2 = EBook('epub', '40', 'https://mybooks/ebook2.com', 'best of 1990', 'Aleksievich', 2222222222222, 20)
e_book_3 = EBook('fb2', '50', 'https://mybooks/ebook3.com', 'best of 2000', 'Arlou', 3333333333333, 30)

class PhysicalBook(Book):
    def __init__(self, weight, in_stock, title, author, ISBN, price):
        super().__init__(title, author, ISBN, price)
        self.__weight = weight
        self.in_stock = in_stock

    def __set_weight(self, weight):
        self.__weight = weight
        if __weight > 0:
            return self.__weight == weight
        else:
            print("Error, the weight can't be <= 0!")
    def get_weight(self):
        return self.__weight

    def get_in_stock(self, in_stock):
        if self.in_stock > 0:
            return True
        else:
            return False
            print(f"{self.in_stock} is not available")

ph_book_1 = PhysicalBook('150', '5', 'best of 1980', 'Bykau', 1111111111111, 10)
ph_book_2 = PhysicalBook('200', '10', 'best of 1990', 'Aleksievich', 2222222222222, 20)
ph_book_3 = PhysicalBook('250', '15', 'best of 2000', 'Arlou', 3333333333333, 30)

class Customer:
    def __init__(self, name, email, address):
        self.__name = name
        self.email = email
        self.address = address

    def get_name(self):
        return self.__name

    def __set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.email

    def __set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.address

    name = property(get_name)
    email = property(get_email, __set_email)
    address = property(get_address, __set_address)

customer_1 = Customer('Andre', 'andre@gmail.com', 'Minsk')
customer_2 = Customer('Ben', 'ben@gmail.com', 'Pinsk')
customer_3 = Customer('Dan', 'dan@gmail.com', 'Slutsk')

class ShoppingCart:
    CART = []
    def __init__(self, cust_name, add, remove, total_cost):
        self.customer_name = cust_name
        self.addition = add
        self.remove = remove
        self.total_cost = total_cost

    def add_book(self, book, count):
        self.book = book
        self.count  = count
        CART.append(Book(book_i))

    def remove_book(self, book, count):
        self.book = book
        self.count  = count
        CART.remove(Book(book_i))

    def total_cost(self, price, count):
        self.price = price
        self.count  = count
        total_cost = self.price(i)*self.count(i)
        return total_cost

class PremiumCustomer(Customer):
    def __init__(self, name, email, address, status, discount):
        super().__init__(name, email, address)
        self.status = status
        self.discount = discount

    def get_status(self, name, status):
        self.name = name
        self.status = status

    def set_discount(self, status, discount):
        if status == premium:
            # discount == 0.1 => disc_price = (1 - discount)*price
            self.discount == 0.1
        else:
            self.discount == 0
    def get_discount(self, status, discount):
        self.discount = discount
        self.status = status

class Order:
    def __init__(self, list_of_books, total_price):
        self.list_of_items = list_of_books
        self.total_price = total_price

    def set_list_of_books(self, list_of_books):
        self.ShoppingCart.CART = list_of_books

    def total_price(self, price, count):
        self.price = price
        self.count  = count
        total_price = self.price(i)*self.count(i)
        return total_price














